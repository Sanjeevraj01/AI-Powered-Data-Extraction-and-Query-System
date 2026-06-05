import cv2
import pytesseract
import numpy as np
from PIL import Image
import os


# Windows Example
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )


def preprocess_image(image_path: str):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to load image")

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Noise reduction
    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Adaptive threshold
    processed = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return processed


def extract_text_from_image(
    image_path: str
):

    try:

        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"{image_path} not found"
            )

        processed_image = preprocess_image(
            image_path
        )

        text = pytesseract.image_to_string(
            processed_image,
            config="--psm 6"
        )

        return text.strip()

    except Exception as e:
        raise Exception(
            f"OCR Error: {str(e)}"
        )