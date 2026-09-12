import cv2
import numpy as np

def draw(event, x, y, flags, param):

    if event == cv2.EVENT_MOUSEMOVE:
        print("mouse moved")

    elif event == cv2.EVENT_LBUTTONDOWN:
        print("left button down")

    elif event == cv2.EVENT_RBUTTONDOWN:
        print("right button down")
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('q'):
        break

cv2.destroyAllWindows()