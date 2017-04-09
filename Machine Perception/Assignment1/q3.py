#Convert BGR to Lab
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.jpg')
  
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2Lab) #Conversion Lab image
L, a, b =cv2.split(lab_image) #Split into channels

#Saving the images
cv2.imwrite('Ligthness.jpg', L)
cv2.imwrite('a.jpg', a)
cv2.imwrite('b.jpg', b)

cv2.imshow('Lightness', L)
cv2.imshow('A*', a)
cv2.imshow('B*', b)



cv2.waitKey(0)
cv2.destroyAllWindows()
