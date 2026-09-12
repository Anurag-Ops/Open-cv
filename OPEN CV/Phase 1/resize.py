import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

# img = cv2.resize(image, (800, 600))
# if you want to resize the image to a specific width and height, you can use the above line.
# if you want to resize the image while maintaining the aspect ratio, you can use the following code:
if image is not None:
    height, width = image.shape[:2]
    new_width = 800
    new_height = int((new_width / width) * height)
    img = cv2.resize(image, (new_width, new_height))
    cv2.imshow('Resized Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
