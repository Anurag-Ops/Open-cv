import cv2
import numpy as np

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1], 
                            [0, -1, 0]])

sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


