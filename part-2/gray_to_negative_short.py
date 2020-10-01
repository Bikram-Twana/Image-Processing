import matplotlib.pyplot as plt

img = plt.imread('image/panda.jpg')

plt.imshow(255 - img, cmap="gray")
plt.show()
