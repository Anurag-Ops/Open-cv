import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)  
cv2.waitKey(0)
cv2.destroyAllWindows()