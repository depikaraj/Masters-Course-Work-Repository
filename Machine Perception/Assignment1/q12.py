# Classify images into modes : Potrait, Landscape and Night
import cv2
import numpy as np
import glob

im = [] #Array declaration
responses = []

#Reading images from file
#Read landscape type images
for img in glob.glob("/home/jarvis/mp/assugnment1/que12/landscape/*.jpg"):
    n= cv2.imread(img)
    im.append(n)
    responses.append(1) #Class = Landscape
    

#Read night type images
for img in glob.glob("/home/jarvis/mp/assugnment1/que12/night/*.jpg"):
    n= cv2.imread(img)
    im.append(n)
    responses.append(2) #Class = Night

#Read potrait type images
for img in glob.glob("/home/jarvis/mp/assugnment1/que12/potrait/*.jpg"):
    n= cv2.imread(img)
    im.append(n)
    responses.append(3) #Class = Potrait


length = len(im) #total no. of images


#Classification of data into two sets of length equal to no. of images
#Declaring arrays of type float 32 
trainData = np.empty([length,12288], dtype=np.float32)
testData = np.empty([length,12288], dtype=np.float32)

#Converting images to float32 data type
for j in range(length):
	im[j] = np.array(im[j]).astype(np.float32)
	im[j] = cv2.resize(im[j],(64,64)) #Resize all the images to 64 X 64 size

k = 0
#Read each image into the temporary and flatten to get 1D raw pixels
for i in range(length):
	temp = np.array(im[i]) #Temporary var
	flatten = temp.flatten() 
	trainData[i] = flatten #Load the raw pixels into train data array
	
#convert responses to float32 data type
responses = np.array(responses).astype(np.float32)

#Declare new test input for classification
#new = cv2.imread('new1.jpeg')
#new = cv2.imread('new2.jpeg')
new = cv2.imread('new3.jpeg')
new = cv2.resize(new,(64,64)) #Resize the new image 

#Store the test input in temp var, flatten it and convert into float 32 data type
temp2 = np.array(new) 
fl = temp2.flatten() 
fl = fl.astype(np.float32)

for i in range(length):
	testData[i] = fl


# Call KNN function with k =11 neighbours
knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)
ret, results, neighbours ,dist = knn.findNearest(testData, 11)

#Print the results
print(neighbours)

if results[0] == 1:
	print("Its a landscape image")
elif results[0] == 2:
	print("Its a night image")
else:
	print("Its a potrait image")

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


