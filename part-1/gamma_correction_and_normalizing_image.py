	
import numpy as np
import cv2

img = cv2.imread('/home/vikram/Documents/bbb/qwr.jpeg')
# Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_two_point_two = np.array(255*(img/255)**2.2,dtype='uint8')

# Display the images in subplots
img3 = cv2.hconcat([gamma_two_point_two])
cv2.imshow('a2',img3)
cv2.waitKey(0)
