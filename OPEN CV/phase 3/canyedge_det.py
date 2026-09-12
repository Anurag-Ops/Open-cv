import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 200)
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

