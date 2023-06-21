import cv2
import numpy as np
from pyzbar import pyzbar
from datetime import datetime
import qrcode
import pytz

class QRCode:
    def read(image):

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

    def make(id):
        eastern = pytz.timezone('US/Central')

        now = datetime.now(eastern)

        # Format each component as a two-digit number
        twoDigitSeconds = str(int(now.second)-4).zfill(2)
        twoDigitMinutes = str(now.minute).zfill(2)
        twoDigitHours = str(now.hour).zfill(2)
        twoDigitDay = str(now.day).zfill(2)
        twoDigitMonth = str(now.month).zfill(2)

        # Concatenate the components to create the integer
        timeInteger = int(twoDigitSeconds + twoDigitMinutes + twoDigitHours + twoDigitDay + twoDigitMonth)

        qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
        )

        qr_code.add_data(id + "@" + str(timeInteger))

        qr_code.make(fit=True)

        return qr_code.make_image(fill_color="black", back_color="white")