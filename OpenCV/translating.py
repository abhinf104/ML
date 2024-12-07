import cv2
import numpy as np

def rotate_image(image, angle, scale=1.0):
    center = (image.shape[1] // 2, image.shape[0] // 2)  # Center of the image
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

def translate_image(image, tx, ty):
    translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# Load the image
image_path = './image/SampleJPGImage_50kbmb.jpg'
image = cv2.imread(image_path)

# Rotate the image
angle = 45  # Rotation angle in degrees
rotated_image = rotate_image(image, angle)

# Translate the image
tx, ty = 50, 50  # Translation in x and y directions
translated_image = translate_image(image, tx, ty)

# Flip the image
flip_code = 1  # 0 for vertical, 1 for horizontal, -1 for both axes
flipped_image = flip_image(image, flip_code)

# Display the results
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
