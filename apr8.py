import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("sample.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

# Display
titles = ["Original", "Grayscale", "Blurred", "Edges"]
images = [image_rgb, gray, blur, edges]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()