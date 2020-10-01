import matplotlib.pyplot as plt 
import numpy as np 
from my_modules import mean_filter, gaussian_noise
import cv2

img = plt.imread('rice.png')

def gaussian_noise(image):

    row,col = image.shape
    mean = 0
    var = 0.01
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = image + gauss
    return noisy

guss_image = gaussian_noise(img)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Noise", guss_image)
# cv2.waitKey(0)
# plt.imshow(guss_image, cmap="gray")
# plt.show()

#applying mean_filter on Gaussian_noise_image
mean = mean_filter(guss_image)
cv2.imshow("Arithmetic Mean on Gaussian Noise", mean)
cv2.waitKey(0)