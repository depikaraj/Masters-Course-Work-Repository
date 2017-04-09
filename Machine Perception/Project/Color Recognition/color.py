from PIL import Image
import scipy
import scipy.cluster
from pprint import pprint
import scipy.misc
import codecs
import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import hex2color, rgb2hex
#import webcolors
#import pyttsx

image = Image.open('4.jpg')
NUM_CLUSTERS = 5

# Convert image into array of values for each point.
ar = scipy.misc.fromimage(image)
shape = ar.shape
print (shape)

# Reshape array of values to merge color bands.
if len(shape) > 2:
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

print (ar.shape)
# Get NUM_CLUSTERS worth of centroids.

codes,_= scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

print(codes)

# Pare centroids, removing blacks and whites and shades of really dark and really light.
original_codes = codes
for low, hi in [(60, 200), (35, 230), (10, 250)]:
    codes = scipy.array([code for code in codes 
                         if not ((code[0] < low and code[1] < low and code[2] < low) or
                                 (code[0] > hi and code[1] > hi and code[2] > hi))])
    if not len(codes): codes = original_codes
    else: break
codes= codes.astype(int)
print(codes)


# Assign codes (vector quantization). Each vector is compared to the centroids
# and assigned the nearest one.
vecs, _ = scipy.cluster.vq.vq(ar, codes)#index of the code array closest in ar
print(vecs)

# Count occurences of each clustered vector.
counts, bins = scipy.histogram(vecs, len(codes))

print(bins,counts)
codes1=codes/255
print(codes1)

colors=[rgb2hex(code) for code in codes1]
print(colors)

total = scipy.sum(counts)
print(total)
color_dist = dict(zip(colors, [count/float(total) for count in counts]))
pprint(color_dist)

# Find the most frequent color, based on the counts.
index_max = scipy.argmax(counts)
print(index_max)

peak = codes[index_max]
print(peak)

color = rgb2hex(peak/255)
print(webcolors.rgb_to_name(peak))
'''
engine = pyttsx.init()
engine.say('The dominant color is',webcolors.rgb_to_name(peak))
engine.runAndWait()
'''
