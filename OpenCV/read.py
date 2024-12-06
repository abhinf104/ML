import cv2

# Read the image from file --> frame -> array of pixels{B G R values}->shape of the array is (height, width, 3)
image = cv2.imread('./image/SampleJPGImage_200kbmb.jpg')

print(image.shape)

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Open the video file
cap=cv2.VideoCapture("./video/SampleVideo_1280x720_1mb.mp4")


while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Display the frame in a window
    cv2.imshow('Video', frame)
    
    # Wait for 25ms and break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()