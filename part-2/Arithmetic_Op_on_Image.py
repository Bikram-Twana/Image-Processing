import matplotlib.pyplot as plt



imgA = plt.imread('image/cameraman.png')
imgB = plt.imread('image/rice.png')

# print(type(img1))
# print(img1.shape)
# print(img1.ndim)
# print(img1.size)
# print(img1.dtype)
# print(img1.nbytes)

# print(img1[10, 10, 1])

# Addition
def addition(imageA, imageB):
    img = imageA + imageB
    return img

# Subtraction A-B
def subtraction_A_TO_B(imageA, imageB):
    img = imageA - imageB
    return img
# Subtraction B-A
def subtraction_B_TO_A(imageA, imageB):
    img = imageB - imageA
    return img

# Division A/B
def division_A_TO_B(imageA, imageB):
    img = imageA / imageB
    return img
# Division B/A
def division_B_TO_A(imageA, imageB):
    img = imageB / imageA
    return img

# Multiplication A*B
def multiplication(imageA, imageB):
    img = imageA * imageB
    return img    

outputs = [imgA, imgB, addition(imgA, imgB), subtraction_A_TO_B(imgA, imgB), subtraction_B_TO_A(imgA, imgB), division_A_TO_B(imgA, imgB), division_B_TO_A(imgA, imgB), multiplication(imgA, imgB)]
titles = ["cameraman", "rice", "add", "sub_A_TO_B", "sub_B_TO_A", "div_A_TO_B", "div_B_TO_A", "mul"]

for i in range(8):
    plt.subplot(1, 8, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


#turning into image negative
# plt.imshow(np.bitwise_not(img1))
# plt.show()