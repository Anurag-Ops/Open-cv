import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')
if image is not None:
    h, w, c = image.shape
    print(f"Image dimensions: Width = {w}, Height = {h}")

else:
    print("Error: Image not found or unable to load.")

     