import cv2
import numpy as np
from pyzbar import pyzbar

def read_qr_code(image):

    image_data = image.read()
    # Convert the image data to numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Decode the image array
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pyzbar to scan the QR code
    qr_codes = pyzbar.decode(gray)


    return qr_codes[0].data.decode("utf-8")