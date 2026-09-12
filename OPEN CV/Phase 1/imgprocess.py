import cv2

image = cv2.imread(r'C:\OPEN CV\Phase 1\Screenshot 2026-08-17 205434.png')

if image is not None:
    img1 = image[:, :, 0]  # Extract the first channel (Blue channel)
    img2 = image[:, :, 1]  # Extract the second channel (Green channel)
    img3 = image[:, :, 2]  # Extract the third channel (Red channel)

    cv2.imshow('Channel 1 (Blue)', img1)
    cv2.imshow('Channel 2 (Green)', img2)
    cv2.imshow('Channel 3 (Red)', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:   
    print("Error: Image not found or unable to load.")
