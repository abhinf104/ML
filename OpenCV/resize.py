import cv2

def resize_image(image_path,width=None,height=None,interpolation=cv2.INTER_NEAREST):
    # Read the image from file
    image = cv2.imread(image_path)
    
    # Get the original dimensions
    (h, w) = image.shape[:2]
    
    # If both width and height are None, return the original image
    if width is None and height is None:
        return image
    # Calculate the aspect ratio and resize dimensions
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        ratio = height / float(h)
        dim = (int(w * ratio), height)
    else:
        # Calculate the ratio of the width and construct the dimensions
        ratio = width / float(w)
        dim = (width, int(h * ratio))
    resized = cv2.resize(image,dim,interpolation=interpolation)
    return resized

interpollationArr = [cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LINEAR, cv2.INTER_LANCZOS4]
window_names = ["INTER_AREA", "INTER_CUBIC", "INTER_LINEAR", "INTER_LANCZOS4"]

for interpolation, window_name in zip(interpollationArr, window_names):
    resized = resize_image("./image/SampleJPGImage_100kbmb.jpg", width=500, height=500, interpolation=interpolation)
    cv2.imshow(window_name, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

