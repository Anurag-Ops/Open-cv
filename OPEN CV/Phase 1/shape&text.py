import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 3)

cv2.circle(img, (400, 400), 50, (0, 0, 255), -1)

cv2.putText(img, 'OpenCV', (120, 250),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow('Shape and Text', img)

cv2.waitKey(0)
cv2.destroyAllWindows()