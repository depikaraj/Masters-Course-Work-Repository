
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

#reading in an image
image = cv2.imread('road6.jpeg')
plt.imshow(image)
cv2.imshow('Original', image)

#Converting to gray image
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Applies the Canny transform   
def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

#Applies a Gaussian Noise kernel
def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


#Applies an image mask.Only keeps the region of the image defined by the polygon formed from `vertices`.The rest of the image is set to black.
def region_of_interest(img, vertices):

    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

#Function for drawing green lines
def draw_lines(img, lines):  
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 10)

#Hough Probablistic function
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    return lines

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    return cv2.addWeighted(initial_img, α, img, β, λ)

#Flow of events for lane detection
def pipeline(image):  
    #Parameters for region of interest
    '''
    road.png	
    bot_left = [230, 330]
    bot_right = [270, 330]
    apex_right = [250, 150]
    apex_left = [240, 160]
    
    #raod3.png
    bot_left = [164, 530]
    bot_right = [790, 488]
    apex_right = [529, 337]
    apex_left = [440, 337]
   
    #road4.png
    bot_left = [46, 177]
    bot_right = [222, 176]
    apex_right = [154, 98]
    apex_left = [130, 98]
    
    #road5.jpg
    bot_left = [87, 191]
    bot_right = [214, 193]
    apex_right = [135, 75]
    apex_left = [115, 75]
    '''
    #road6.jpg
    bot_left = [121, 188]
    bot_right = [129, 188]
    apex_right = [133, 110]
    apex_left = [134, 110]
    	
    v = [np.array([bot_left, bot_right, apex_right, apex_left], dtype=np.int32)]
    
    
    #Run canny edge dection and mask region of interest
    gray = grayscale(image)
    blur = gaussian_blur(gray, 11)
    edge = canny(blur, 50, 125)
    cv2.imshow('after canny', edge)
    
    lines = hough_lines(edge, 0.8, np.pi/180, 25, 10, 200)
    print(lines)
    line_img = np.copy((image)*0) # full black image
    cv2.imshow('After line_img', line_img)
    draw_lines(line_img, lines)
    cv2.imshow('Black with red line',line_img)
    
    line_img = region_of_interest(line_img, v)
    final = weighted_img(line_img, image)
    cv2.imshow('final', final)

    return final

plt.show()
output = pipeline(image)

#Saving the outputs
cv2.imshow('Output', output)
cv2.imwrite('Output_road.jpg', output)

cv2.waitKey(0)
cv2.destroyAllWindows()
