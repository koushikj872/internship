import cv2

# Load image
image = cv2.imread("sample.jpg")

# Display shape
print("Image Shape:", image.shape)

# Height, Width, Channels
height, width, channels = image.shape

print("Height:", height)
print("Width :", width)
print("Channels:", channels)

# Print pixel value at position (100,100)
print("\nPixel Value at (100,100):")
print(image[100, 100])

# Print first 5x5 pixel values
print("\nFirst 5x5 Pixels:")
print(image[:5, :5])