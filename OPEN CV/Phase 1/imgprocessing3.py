import cv2
import numpy as np

flag = False
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global ix, iy, flag

    if event == cv2.EVENT_LBUTTONDOWN:
        flag = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flag:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        flag = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)   # THIS WAS MISSING

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('q'):
        break

cv2.destroyAllWindows()