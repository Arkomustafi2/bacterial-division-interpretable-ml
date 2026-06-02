import numpy as np
from skimage import restoration

def normalize_image(img):
    img = img.astype('float32')
    mean = img.mean()
    std = img.std()
    if std < 1e-8:
        return img * 0
    return (img - mean) / std

def subtract_background(img, radius=50):
    """
    Rolling-ball background subtraction.
    """
    img_shifted = img - img.min()

    background = restoration.rolling_ball(
        img_shifted,
        radius=radius
    )

    corrected = img_shifted - background

    return corrected

def preprocess_image(img, radius=50):
    # Step 1: convert and normalize roughly
    img = img.astype('float32')

    # Step 2: background subtraction
    img_clean = subtract_background(img, radius=radius)

    # Step 3: FINAL normalization
    img_final = normalize_image(img_clean)

    return img_final