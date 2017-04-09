#Detect a 45 degree line 

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lines.png')

# generating the kernels
kernel = np.array([[-1,-1,2], [-1,2,-1], [2,-1,-1]]) 
output = cv2.filter2D(img, -1, kernel) #Filter for detecting 45 degree line

#plotting using matplotlib
plt.subplot(221), plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow( output,"gray")
plt.title('45 Degree Detector'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

