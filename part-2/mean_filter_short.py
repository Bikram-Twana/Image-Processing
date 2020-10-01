import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('image/lena.bmp')

kernel = np.array(np.ones((7, 7), np.float32))/49
output = cv.filter2D(img, -1, kernel)

outputs = [img, output]
titles = ["Original", "Mean Filter (7*7)"]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.axis(False)
plt.show()