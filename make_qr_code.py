from PIL import Image
from datetime import datetime
import qrcode
import pytz


def make_qr_code(id):

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

    print(timeInteger)
    qr_code.add_data(id + "@" + str(timeInteger))
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")

    return (img, timeInteger)


