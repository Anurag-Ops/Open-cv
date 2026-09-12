import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('thresholded image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

