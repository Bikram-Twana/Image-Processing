#discrete cosine transform

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.colors import Normalize
# import matplotlib.cm as cm

# B=8 #blocksize
# fn3= 'new13.jpg'
# img1 = cv2.imread(fn3,cv2.IMREAD_GRAYSCALE)
# h,w=np.array(img1.shape[:2])//B * B
# print(h)
# print(w)
# img1=img1[:h,:w]
# blocksV=h/B
# blocksH=w/B
# vis0 = np.zeros((h,w))
# Trans = np.zeros((h,w))
# vis0[:h, :w] = img1
# for row in range(int(blocksV)):
#         for col in range(int(blocksH)):
#              currentblock = cv2.dct(vis0[row*B:(row+1)*B,col*B:(col+1)*B])
#              Trans[row*B:(row+1)*B,col*B:(col+1)*B]=currentblock

# cv2.imshow("trans",Trans)
# cv2.waitKey(0)


# # Discrete Fourier Transform
# import cv2
# import numpy as np
# from PIL import Image

# img1 = cv2.imread("s1.jpg", cv2.IMREAD_GRAYSCALE)
# f = np.fft.fft2(img1)

# # shifting result by N/2 to bring in center
# fshift = np.fft.fftshift(f)
# # The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.
# mag_spec = 20 * np.log(np.abs(fshift))
# mag_spec = np.asarray(mag_spec, dtype=np.uint8)
# cv2.imshow(" Original Image ", img1)

# cv2.imshow("After log transform Dft", mag_spec)

# # rotation
# img_rtr = Image.open("s1.jpg")
# rotate = img_rtr.rotate(45)

# rotate.show()

# f2 = np.fft.fft2(rotate)

# # shifting result by N/2 to bring in center
# fshift2 = np.fft.fftshift(f2)
# # The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.
# mag_spec2 = 20 * np.log(np.abs(fshift2))
# mag_spec2 = np.asarray(mag_spec2, dtype=np.uint8)
# cv2.imshow(' Rotation', mag_spec2)
# # image translation
# num_rows, num_cols = img1.shape[:2]

# translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
# img_translation = cv2.warpAffine(img1, translation_matrix, (num_cols + 70, num_rows + 110))
# cv2.imshow(' Translation', img_translation)

# f1 = np.fft.fft2(img_translation)

# # shifting result by N/2 to bring in center
# fshift1 = np.fft.fftshift(f1)
# # The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks.
# mag_spec1 = 20 * np.log(np.abs(fshift1))
# mag_spec1 = np.asarray(mag_spec1, dtype=np.uint8)

# cv2.imshow('Translation', mag_spec1)

# cv2.waitKey(0)





import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('s1.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


img1 = cv2.imread("new13.jpg", cv2.IMREAD_GRAYSCALE)
f1 = np.fft.fft2(img1)
cv2.imshow("abc",f1)