from skimage.filters import threshold_local
from PIL import Image
import numpy as np
import cv2, base64, requests, json

class ML_model():
    def __init__(self):
        pass
        
    def get_receipt_items(self, base64_image):
        """
        params:
            - img
            A base 64 encoded image to be inferences

        return: 
            python dictionary of the receipt items

        TODO - make this function have 2 subroutines
        1) preprocess image
        2) make inference

        Also remove the generation of unneeded files
        or at least remove the files after they are
        created
        """
        decoded_bytes = base64.b64decode(base64_image)
        output_path = 'output.jpg'  # Specify the path and filename for the output image

        with open(output_path, 'wb') as file:
            file.write(decoded_bytes)

        file_name = "output.jpg"
        img = Image.open("output.jpg")

        def resize_img(img, scale):
            img = np.array(img)
            width = int(img.shape[1] * scale / 100)
            height = int(img.shape[0] * scale / 100)
            dsize = (width, height)
            return cv2.resize(img, dsize=dsize)

        img = resize_img(img,300)

        def opencv_resize(image, ratio):
            width = int(image.shape[1] * ratio)
            height = int(image.shape[0] * ratio)
            dim = (width, height)
            return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


        image = cv2.imread(file_name)
        resize_ratio = 500 / image.shape[0]
        original = image.copy()
        image = opencv_resize(image, resize_ratio)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        dilated = cv2.dilate(blurred, rectKernel)
        edged = cv2.Canny(dilated, 100, 200, apertureSize=3)
        contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       
        largest_contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

        def approximate_contour(contour):
            peri = cv2.arcLength(contour, True)
            return cv2.approxPolyDP(contour, 0.032 * peri, True)

        def get_receipt_contour(contours):    
            for c in contours:
                if len(approximate_contour(c)) == 4:
                    return approximate_contour(c)

        receipt_contour = get_receipt_contour(largest_contours)
    
        def contour_to_rect(contour):
            pts = contour.reshape(4, 2)
            rect = np.zeros((4, 2), dtype = "float32")
    
            s = pts.sum(axis = 1)
            rect[0] = pts[np.argmin(s)]
            rect[2] = pts[np.argmax(s)]
        
            diff = np.diff(pts, axis = 1)
            rect[1] = pts[np.argmin(diff)]
            rect[3] = pts[np.argmax(diff)]
            return rect / resize_ratio

        def wrap_perspective(img, rect):
            (tl, tr, br, bl) = rect
            widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
            widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        
            heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
            heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

            maxWidth = max(int(widthA), int(widthB))
            maxHeight = max(int(heightA), int(heightB))

            dst = np.array([
                [0, 0],
                [maxWidth - 1, 0],
                [maxWidth - 1, maxHeight - 1],
                [0, maxHeight - 1]], dtype = "float32")
            
            M = cv2.getPerspectiveTransform(rect, dst)
            
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

        API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTNiYzg0YWEtYjA2NC00Yjk2LThhNzktYTNhYzc2ZjFmNzRmIiwidHlwZSI6ImFwaV90b2tlbiIsIm5hbWUiOiJkdWRlIiwiaXNfY3VzdG9tIjp0cnVlfQ.kX9MbCPA6F0Gfdd_X9otWcnxojn4ddywqfA6NjW0jdM"
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.post(url, files=files, data=payload, headers=headers)
        data = json.loads(response.text)
        
        print(f'response {response}')
        pre_json_array = []
        for item in data['amazon']['extracted_data'][0]['item_lines']:
            data_to_add = {'Product Name': item['description'], 
                            'Price': item['amount']
                            }
            pre_json_array.append(data_to_add)

        return pre_json_array
    
# image = "monster.jpg"

# with open(image, "rb") as file:
#     image_data = file.read()
    
# img = base64.b64encode(image_data)
# model = ML_model()
# print(model.get_receipt_items(img))