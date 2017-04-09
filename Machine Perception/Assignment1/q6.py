import numpy as np
import cv2
from matplotlib import pyplot as plt

#Definition of Gaussian Blurring function
def Blurring(sizeOfKernel, howManyTimes, givenIMG, sigmax):
    for x in range(howManyTimes):
        givenIMG = cv2.GaussianBlur(givenIMG, sizeOfKernel, sigmax)
    return givenIMG  #End of the function

img = cv2.imread("low3.jpeg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #conversion from bgr to rgb for plotting using matplotlib
GBImage1 = Blurring((3,3), 1, img, 1)   #Kernel size 3x3 and sigma = 1
GBImage2 = Blurring((11,11), 1, img, 2) #Kernel size 11x11 and sigma = 2
GBImage3 = Blurring((21,21), 1, img, 3) #Kernel size 21x21 and sigma = 3


#Plotting using matplotlib
plt.subplot(221), plt.imshow(img2)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(GBImage1)
plt.title('Kernel 3x3 SD = 1'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(GBImage2)
plt.title('Kernel 11X11 SD = 2'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(GBImage3)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.title('Kernel 21x21 SD = 3')
plt.suptitle('Gaussian Blurring', size = 18)


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
