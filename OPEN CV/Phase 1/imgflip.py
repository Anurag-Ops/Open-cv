import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')
imge = cv2.flip(image, 1)  # Flip the image horizontally & 0 for the vertical axis
cv2.imshow('Flipped Image', imge)
cv2.waitKey(0)
cv2.destroyAllWindows()