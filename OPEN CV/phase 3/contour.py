import cv2

# Image path — apne actual path ke according change karo
img = cv2.imread(r"C:\OPEN CV\phase 3\feature_hu_386ed0a3232a6c46.png")
# Check if image loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw original contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:

    # Approximate contour
    approx = cv2.approxPolyDP(
        contour,
        0.01 * cv2.arcLength(contour, True),
        True
    )

    # Get first point
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # Detect shape
    if len(approx) == 3:
        cv2.putText(
            img, "Triangle",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    elif len(approx) == 4:
        cv2.putText(
            img, "Quadrilateral",
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    # Draw approximated contour
    cv2.drawContours(
        img,
        [approx],
        -1,
        (0, 0, 255),
        5
    )

    # Vertices text
    cv2.putText(
        img,
        f"Vertices: {len(approx)}",
        (x, y + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        2
    )

# Display
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()