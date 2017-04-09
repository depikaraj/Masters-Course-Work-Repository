#BGR to HSL and HSV
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Conversion to rgb for plotting using matplotlib


#HSV
hsv_image2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Conversion from bgr to hsv
hsv = cv2.cvtColor(hsv_image2, cv2.COLOR_BGR2RGB) #Conversion to rgb for plotting using matplotlib
hsv_image = hsv_image2.copy()
h, s, v =cv2.split(hsv_image2)

hsv_image2[:,:,1] = 255 #Setting saturation space to 255
hsv_image2[:,:,2] = 255 #Setting value space to 255
h = cv2.cvtColor(hsv_image2, cv2.COLOR_HSV2RGB)

#Plotting using matplotlib
plt.subplot(3,3,1), plt.imshow(img2)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2), plt.imshow(hsv)
plt.title('HSV Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4), plt.imshow( h,"gray")
plt.title('Hue Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5), plt.imshow( s, "gray")
plt.title('Saturation Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6), plt.imshow(v, "gray")
plt.title('Value channel'), plt.xticks([]), plt.yticks([])


#HSL
hsl_image = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) #Conversion from bgr to hsl
hsl = cv2.cvtColor(hsl_image, cv2.COLOR_BGR2RGB) #Conversion to rgb for plotting using matplotlib
h1, l, s1 = cv2.split(hsl_image)

#Plotting using matplotlib
plt.subplot(3,3,3), plt.imshow(hsl)
plt.title('HSL Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7), plt.imshow( h1,"gray")
plt.title('Hue Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,8), plt.imshow( s1, "gray")
plt.title('Saturation Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,9), plt.imshow(l, "gray")
plt.title('Intensity channel'), plt.xticks([]), plt.yticks([])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
