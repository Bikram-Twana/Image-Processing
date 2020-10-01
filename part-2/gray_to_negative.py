# TO DO:
# need image
# r = intensity value of that pixel position
# S = T(r) which is 255-r
# show those pixel position with new intensity value S


import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('image/test.jpg')

def negative(image):
    row, col = image.shape
    new_image = np.copy(image)
    for i in range(row):
        for j in range(col):
            s = 255 - image[i, j]
            new_image[i, j] = s
    return new_image

output = [img, negative(img)]
titles = ['Original', 'Negative']
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
