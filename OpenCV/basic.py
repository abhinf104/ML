import cv2
import numpy as np

# Load the image
image_path = "./image/SampleJPGImage_100kbmb.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    print("Image loaded successfully")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Blur the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Dilate the image
    kernel = np.ones((2, 2), np.uint8)
    dilated_image = cv2.dilate(edges, kernel, iterations=1)
    
    # Crop the image
    # Define the coordinates of the top-left and bottom-right corners
    x_start, y_start = 50, 50
    x_end, y_end = 200, 200
    cropped_image = image[y_start:y_end, x_start:x_end]

    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Edge Detected Image', edges)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow('Dilated2 Image', dilated_image)
    cv2.imshow('Cropped Image', cropped_image)
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()