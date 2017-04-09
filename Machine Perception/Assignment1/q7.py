#Add Salt and pepper noise remove it by Median filter

import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

#Function definition for adding salt and pepper noise
def AddSAndPNoise (Image, SaltNum, PepperNum):
    CopyImage = Image.copy() 
    nChannel = 0

    #Get Image size
    Width = CopyImage.shape[0]
    Height = CopyImage.shape[1]
 
    #If image is grayscale, it will not have Image.shape[2] so it raises IndexError exception
    try:
        nChannel = CopyImage.shape[2]
    except IndexError: #Handling of exception
        nChannel = 1

    #Make Salt Noise
    for Salt in range(0, SaltNum):
    #Generate Random Position
        RWidth = random.randrange(0, Width)
        RHeight = random.randrange(0, Height)
    #Make Noise
        if nChannel > 1: #Proceed if its a color image
            for c in range(0, nChannel):
                CopyImage[RWidth, RHeight, c] = 255
        else:
           CopyImage[RWidth, RHeight] = 255

    #Make Pepper Noise
    for Pepper in range(0, PepperNum):
    #Generate Random Position
        RWidth = random.randrange(0, Width)
        RHeight = random.randrange(0, Height)
    #Make Noise
        if nChannel > 1:
            for c in range(0, nChannel):
                CopyImage[RWidth, RHeight, c] = 0
        else:
            CopyImage[RWidth, RHeight] = 0

    return CopyImage  #End of function

img = cv2.imread('image1.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Conversion from bgr to rgb for plotting using matplotlib

img3 = AddSAndPNoise(img2, 100, 500) #Adding salt and pepper noise to image
median = cv2.medianBlur(img3,5) #Removing the noise using Median Blurring

#Plotting using matplotlib
plt.subplot(131), plt.imshow(img2)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img3)
plt.title('With salt & pepper noise'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(median)
plt.title('After Filtering'), plt.xticks([]), plt.yticks([])
plt.suptitle('Median Filtering', size = 18)
cv2.imwrite("Saltnpepper.jpg", img2)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()	

