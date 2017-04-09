#Histogram equalization and Whitening

import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
from matplotlib import pyplot as plt

img = cv2.imread('hist.png',0) #Load the gray scale image
plt.hist(img.ravel(),256,[0,256]); plt.show() #Plotting the histogram of input image

#Histogram equalisation

equ = cv2.equalizeHist(img) #Computing histogram equalisation
cv2.imwrite('HistEqua.jpeg', equ)
cv2.imshow('HistEqua Output', equ)
plt.hist(equ.ravel(),256,[0,256]); plt.show() #Plotting the histogram of equalised image

#Whitening
var = np.var(img)
mean = np.mean(img)
height, width = img.shape

img2 = ((img - mean/ (np.sqrt(var))) + img )    #Whitening the image using mean and variance
img3 = cv2.normalize(img2, 0, 255, cv2.NORM_MINMAX) #Normalising the pixel values to range of 0 to 255

cv2.imwrite('Whitening.jpg', img3)
cv2.imshow('White', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
