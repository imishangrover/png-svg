import cv2
import numpy as np

def preprocess_image(image_path, threshold=180):
    image = cv2.imread(str(image_path))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Strong blur to remove noise
    blurred = cv2.medianBlur(gray, 7)

    # Adaptive threshold (VERY IMPORTANT)
    bw = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    #bw = cv2.bitwise_not(bw)

    h, w = bw.shape
    max_size = 800

    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        bw = cv2.resize(bw, None, fx=scale, fy=scale)

    return bw
