#convert bgr to grey scale image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('image1.jpg') #Reading the image
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Conversion from bgr to rgb for plotting using matplotlib
img3 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY) #conversion from rgb to gray scale

#Plotting using matplotlib
plt.subplot(1,2,1),plt.imshow(img2)
plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img3 ,"gray")
plt.title('Gray scale image'), plt.xticks([]), plt.yticks([])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()





