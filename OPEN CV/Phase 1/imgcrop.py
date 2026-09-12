import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')
img_crop = image[100:400, 200:500]  # Crop the image (y1:y2, x1:x2)
cv2.imshow('Cropped Image', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()