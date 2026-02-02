import cv2

# Read image
image = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save output
cv2.imwrite("grayscale_output.jpg", gray)

print("Grayscale image saved successfully")
