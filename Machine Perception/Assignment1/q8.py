#Sobel and Prewitt

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Creating a binary synthetic image (rectangle here)
img = np.zeros((512,512,3), np.uint8) #Create a full black image
cv2.rectangle(img,(200,100),(305,300),(255,255,255),5) #Drawing a white rectangle on black background

#Edge detection using Sobel operator
sobelx = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) #Applying sobel filter of kernel size 5 in x direction
sobely = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) #Applying sobel filter of kernel size 5 in y direction

#Edge detection using Prewitt operator
prewittx = np.array([[2,2,2,2,2],[1,1,1,1,1],[0,0,0,0,0],[-1,-1,-1,-1,-1],[-2,-2,-2,-2,-2]]) #Defining a kernel of size 5 for Prewitt operator
prewitty = np.array([[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2]]) #Defining a kernel of size 5 for Prewitt operator


outputpx = cv2.filter2D(img, -1, prewittx) #Applying prewitt filter of kernel size 5 in x direction
outputpy = cv2.filter2D(img, -1, prewitty) #Applying prewitt filter of kernel size 5 in y direction

#Plotting using matplotlib
plt.subplot(2,3,1), plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2), plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3), plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4), plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5), plt.imshow(outputpx,cmap = 'gray')
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6), plt.imshow(outputpy,cmap = 'gray')
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
