
# # first_code inversion

# from PIL import Image , ImageDraw
# import PIL.ImageOps  
# image = Image.open('abcd.jpg')

# inverted_image = PIL.ImageOps.invert(image)

# # # to fill text on image
# # img_draw = ImageDraw.Draw(inverted_image)
# # img_draw.text((50,450),'BIKRAM TWAYANA' , fill ='red' )

# inverted_image.save('inverted_abcd.jpg')











# # second_code_gamma_correction

# import numpy as np
# from PIL import Image

# import matplotlib.pyplot as plt 

# gray_img = Image.open('qwr.jpeg').convert("LA")
# gray_img.save("lenna_gray.png")#grayscale
# row = gray_img.size[0]
# col = gray_img.size[1]
# gamma1 = 0.88
# gamma2 = 2.2
# result_img1 = Image.new("L", (row, col))
# result_img2 = Image.new("L", (row, col))
# for x in range(1 , row):
#     for y in range(1, col):
#         value = pow(gray_img.getpixel((x,y))[0]/255,(1/gamma1))*255
#         if value >= 255 :
#             value = 255
#         result_img1.putpixel((x,y), int(value))
#         value = pow(gray_img.getpixel((x,y))[0]/255,(1/gamma2))*255
#         if value >= 255 :
#             value = 255
#         result_img2.putpixel((x,y), int(value))
# result_img1.save("gamma_088.png")
# result_img2.save("gamma_115.png")

# plt.figure(figsize=(15,10))
# y = gray_img.histogram()
# y = y[0:256]
# x = np.arange(len(y))
# plt.subplot(221)
# plt.title("lenna gray hist")
# plt.bar(x, y)

# plt.subplot(222)
# y = result_img1.histogram()
# x = np.arange(len(y))
# plt.title("gamma 0.88 hist")
# plt.bar(x, y)

# plt.subplot(223)
# y = result_img2.histogram()
# x = np.arange(len(y))
# plt.title("gamma 1.15 hist")
# plt.bar(x, y)

# fig = plt.gcf()
# plt.show()

# fig.savefig('lenna_gamma_correction_hist.png')
