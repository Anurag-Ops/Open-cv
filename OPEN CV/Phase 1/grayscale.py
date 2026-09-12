import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")