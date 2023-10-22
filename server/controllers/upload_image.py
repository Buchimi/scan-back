from flask import Flask

@app.route('api/upload', methods=['POST'])
def upload_image():
    # Get the base64 encoded image from the request payload
    data = request.get_json()
    base64_image = data.get('image_data')

    # Your processing code for the base64 image can go here
    # For example, you can decode the base64 image and save it to a file
    # or perform image processing operations on it

    response = {}

    # return the json of the prices that
    return base64_image