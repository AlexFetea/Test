import cv2
import numpy as np
from pyzbar import pyzbar
from datetime import datetime
import qrcode
import pytz
from QRCode import QRCode
from flask_cors import CORS
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime


def BuildImage(id):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the background image
    background_image = Image.open(os.path.join(current_dir, 'actual.jpg'))

    qr_code = QRCode.make(id)

    qr_code = qr_code.resize((1060, 1060))

    image_with_overlay=qr_code

    # Calculate the position to center the QR code on the background image
    center_x = (background_image.width - qr_code.width) // 2
    center_y = (background_image.height - qr_code.height) // 2 - 420

    # Create a copy of the background image to draw the overlay on
    image_with_overlay = background_image.copy()

    # Paste the QR code image onto the background image
    image_with_overlay.paste(qr_code, (center_x, center_y))

    now = datetime.now()
    # Display time and date
    time_display = now.strftime('%I:%M %p')
    date_display = now.strftime("%B %d{}").format("th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th"))

    draw = ImageDraw.Draw(image_with_overlay)
    text = time_display
    text_font = ImageFont.truetype("arial.ttf", 180)  # Change the font and size as desired
    text_color = (255, 255, 255)  # Change the text color as desired
    text_x = (background_image.width - draw.textlength(text, font=text_font)) // 2
    text_position = (text_x, 1550)  # Change the position of the text as desired
    # Increase the thickness of the text
    text_stroke_width = 5
    # Draw the text with the increased thickness
    draw.text(text_position, text, font=text_font, fill=text_color, stroke_width=text_stroke_width,
              stroke_fill=text_color)

    text = date_display
    text_font = ImageFont.truetype("arial.ttf", 130)  # Change the font and size as desired
    text_color = (0, 0, 0)  # Change the text color as desired
    text_x = (background_image.width - draw.textlength(text, font=text_font)) // 2
    text_position = (text_x, 1830)  # Change the position of the text as desired
    # Increase the thickness of the text
    text_stroke_width = 0
    # Draw the text with the increased thickness
    draw.text(text_position, text, font=text_font, fill=text_color, stroke_width=text_stroke_width,
              stroke_fill=text_color)

    text = "Alex"
    text_font = ImageFont.truetype("arial.ttf", 280)  # Change the font and size as desired
    text_color = (0, 0, 0)  # Change the text color as desired
    text_x = (background_image.width - draw.textlength(text, font=text_font)) // 2
    text_position = (text_x, 1980)  # Change the position of the text as desired
    # Increase the thickness of the text
    text_stroke_width = 3
    # Draw the text with the increased thickness
    draw.text(text_position, text, font=text_font, fill=text_color, stroke_width=text_stroke_width,
              stroke_fill=text_color)
    
    return image_with_overlay