from flask import Flask, request, send_file, render_template, make_response
from QRCode import QRCode
from io import BytesIO
from BuildImage import BuildImage
import logging
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/image/<id>', methods=['GET'])
def return_image(id):

    image_with_overlay = BuildImage(id)
    # Save the resulting image with the overlay
    output_image = BytesIO()
    image_with_overlay.save(output_image, format='JPEG')
    output_image.seek(0)

    # Create a response with cache-control headers
    response = make_response(send_file(output_image, mimetype='image/jpeg'))
    # response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    # response.headers['Pragma'] = 'no-cache'
    # response.headers['Expires'] = '0'
    return response


@app.route('/<id>', methods=['GET'])
def return_page(id):
    return render_template('qrcode.html', id=id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
