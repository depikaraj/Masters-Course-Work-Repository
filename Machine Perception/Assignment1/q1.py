#Get red,blue,green channels of an image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.jpg')
b1, g1, r1 = cv2.split(img)
img2 = cv2.merge([r1,g1,b1]) #Merging needed for plotting using matplotlib
r, g, b =cv2.split(img2)     #To split into into indiviual color spaces

cv2.imwrite('Blue Channel.jpg', b1)
cv2.imwrite('Red Channel.jpg', r1)
cv2.imwrite('Green Channel.jpg', g1)

#Plotting using matplotlib
plt.subplot(2,2,1),plt.imshow(img2)
plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow( r,"gray")
plt.title('Red Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow( g, "gray")
plt.title('Green Channel'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(b, "gray")
plt.title('Blue Channel'),plt.xticks([]), plt.yticks([])
plt.suptitle('Color Channels', size = 18)
plt.show()

k=cv2.waitKey(0)
cv2.destroyAllWindows()

