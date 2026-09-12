import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

if image is not None:
    sucess = cv2.imwrite(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png', image)
    if sucess:
        print("Image saved successfully.")
    else:
        print("Error: Unable to save the image.")

else:
    print("Error: Image not found or unable to load.")
