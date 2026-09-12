import cv2
import numpy as np

img = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')
flag = False
ix, iy = -1, -1
def crop(event, x, y, flags, param):
    global ix, iy, flag
    if event == 1:  # Left mouse button down
        flag = True
        ix, iy = x, y

    elif event == 4:  # Left mouse button up
        flag = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 2)
        cropped_img = img[iy:y, ix:x]
        cv2.imshow("Cropped Image", cropped_img)

cv2.namedWindow('image')
cv2.setMouseCallback('image', crop)


while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('q'):
        break
else:
    cv2.destroyAllWindows()