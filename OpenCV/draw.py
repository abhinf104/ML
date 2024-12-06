import cv2
import numpy as np

# Load an image
image = cv2.imread('./image/SampleJPGImage_200kbmb.jpg')

blank = np.zeros((500, 500, 3), dtype=np.uint8)
# Fill the left half with blue color
blank[:, :250] = (255, 0, 0)  # Blue color in BGR

# Fill the right half with green color
blank[:, 250:] = (0, 255, 0)  # Green color in BGR

cv2.imshow("blank",blank)
cv2.waitKey(0)
cv2.destroyAllWindows()

blank = np.array()
# Draw a line
start_point = (50, 50)
end_point = (200, 200)
color = (255, 0, 0)  # Blue color in BGR
thickness = 10
cv2.line(image, start_point, end_point, color, thickness)

# Draw a rectangle
top_left = (50, 50)
bottom_right = (200, 200)
color = (0, 255, 0)  # Green color in BGR
thickness = 10
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Draw a circle
center = (300, 300)
radius = 50
color = (0, 0, 255)  # Red color in BGR
thickness = 10
cv2.circle(image, center, radius, color, thickness)

# Put text on the image
text = 'Advay'
org = (50, 400)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  # White color in BGR
thickness = 2
cv2.putText(image, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

# Display the image
cv2.imshow('Image with drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()