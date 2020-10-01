import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("image/cameraman.png")

new_img = cv.medianBlur(img, 5)

plt.figure(figsize=(11,6))

plt.subplot(121), plt.imshow(img, cmap="gray"),plt.title("Original")
plt.axis(False)
plt.subplot(122), plt.imshow(new_img, cmap="gray"),plt.title("Median Filter (5*5)")
plt.axis(False)
plt.show()