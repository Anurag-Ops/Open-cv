import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

if image is not None:
    cv2.imshow('Image showing', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")