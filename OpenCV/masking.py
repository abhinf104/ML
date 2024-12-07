import cv2
import numpy as np

# Load the image
image_path = './image/SampleJPGImage_50kbmb.jpg'
image = cv2.imread(image_path)

# Create a mask --> same size , 0 for black and 255 for white
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (image.shape[1] // 2, image.shape[0] // 2), 100, 255, -1)

# Apply the mask to the image
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()