import cv2
import numpy as np
from matplotlib import pyplot as plt

#loading image
img0 = cv2.imread('index.jpeg')

#converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

#remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

#convolution using Laplacian kernel

lap_kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
lap_output = cv2.filter2D(img, -1, lap_kernel)

cv2.imwrite('laplacian.jpg', lap_output)
out = lap_output + gray
cv2.imwrite('sharp.jpg', out)

#Plotting using matplotlib
plt.subplot(1,3,1),plt.imshow(gray, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(lap_output, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(out, cmap='gray')
plt.title('Sharp'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

