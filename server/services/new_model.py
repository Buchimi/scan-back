from skimage.filters import threshold_local
from PIL import Image
import numpy as np
import requests, cv2, base64

class Vision_model():
    def __init__(self):
        self.closure()
        
    def get_receipt_items(self, img):
        """
        receives base 64 image or receipt
        and returns list of dictionaries
        """
        def closure(self):
            with open("base64_image.jpg", "wb") as fh:
                fh.write(base64.decodebytes(img))

            file_name = "base64_image.jpg"
            img = Image.open(file_name)
            img.thumbnail((800,800), Image.ANTIALIAS)

            def resize_img(self, img, scale):
                img = np.array(img)
                width = int(img.shape[1] * scale / 100)
                height = int(img.shape[0] * scale / 100)

                dsize = (width, height)
                return cv2.resize(img, dsize=dsize)

            img = resize_img(img,300)
            def opencv_resize(self, image, ratio):
                width = int(image.shape[1] * ratio)
                height = int(image.shape[0] * ratio)
                dim = (width, height)
                return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


            image = cv2.imread(file_name)
            resize_ratio = 500 / image.shape[0]
            original = image.copy()
            image = self.opencv_resize(image, resize_ratio)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
            dilated = cv2.dilate(blurred, rectKernel)
            edged = cv2.Canny(dilated, 100, 200, apertureSize=3)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0,255,0), 3)
            largest_contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
            # image_with_largest_contours = cv2.drawContours(image.copy(), largest_contours, -1, (0,255,0), 3)

            def approximate_contour(self, contour):
                peri = cv2.arcLength(contour, True)
                return cv2.approxPolyDP(contour, 0.032 * peri, True)

            def get_receipt_contour(self, contours):    
                # loop over the contours
                for c in contours:
                    approx = self.approximate_contour(c)
                    # if our approximated contour has four points, we can assume it is receipt's rectangle
                    if len(approx) == 4:
                        return approx

            receipt_contour = self.get_receipt_contour(largest_contours)
            # image_with_receipt_contour = cv2.drawContours(image.copy(), [receipt_contour], -1, (0, 255, 0), 2)
            # plot_rgb(image_with_receipt_contour)

            def contour_to_rect(contour):
                pts = contour.reshape(4, 2)
                rect = np.zeros((4, 2), dtype = "float32")

                # top-left point has the smallest sum
                # bottom-right has the largest sum
                s = pts.sum(axis = 1)
                rect[0] = pts[np.argmin(s)]
                rect[2] = pts[np.argmax(s)]

                # compute the difference between the points:
                # the top-right will have the minumum difference 
                # the bottom-left will have the maximum difference
                diff = np.diff(pts, axis = 1)
                rect[1] = pts[np.argmin(diff)]
                rect[3] = pts[np.argmax(diff)]
                return rect / resize_ratio

            def wrap_perspective(img, rect):
                # unpack rectangle points: top left, top right, bottom right, bottom left
                (tl, tr, br, bl) = rect

                # compute the width of the new image
                widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
                widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

                # compute the height of the new image
                heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
                heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

                # take the maximum of the width and height values to reach
                # our final dimensions
                maxWidth = max(int(widthA), int(widthB))
                maxHeight = max(int(heightA), int(heightB))

                # destination points which will be used to map the screen to a "scanned" view
                dst = np.array([
                    [0, 0],
                    [maxWidth - 1, 0],
                    [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]], dtype = "float32")
                
                # calculate the perspective transform matrix
                M = cv2.getPerspectiveTransform(rect, dst)
                # warp the perspective to grab the screen
                return cv2.warpPerspective(img, M, (maxWidth, maxHeight))
            
            scanned = wrap_perspective(original.copy(), contour_to_rect(receipt_contour))

            def bw_scanner(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                T = threshold_local(gray, 13, offset = 13, method = "gaussian")
                return (gray > T).astype("uint8") * 255

            result = bw_scanner(scanned)

            output = Image.fromarray(result)
            output.save('result.png')

            url = "https://api.edenai.run/v2/ocr/receipt_parser"

            files = {
                "file": open("result.png", "rb")
            }

            payload = {
                "response_as_dict": True,
                "attributes_as_list": False,
                "show_original_response": False,
                "providers": "amazon",
                "language": "en"
            }

            # API_KEY = get_model_api_key()
            API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTNiYzg0YWEtYjA2NC00Yjk2LThhNzktYTNhYzc2ZjFmNzRmIiwidHlwZSI6ImFwaV90b2tlbiIsIm5hbWUiOiJkdWRlIiwiaXNfY3VzdG9tIjp0cnVlfQ.kX9MbCPA6F0Gfdd_X9otWcnxojn4ddywqfA6NjW0jdM"
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }

            response = requests.post(url, files=files, data=payload, headers=headers)

        return response.text
    

with open("services/test_image.PNG", "rb") as f:
    encoded_image = base64.b64encode(f.read())
    model = Vision_model()
    print(model.get_receipt_items(encoded_image))

