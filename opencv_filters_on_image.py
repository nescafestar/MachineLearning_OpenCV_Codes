# -*- coding: utf-8 -*-
"""OpenCV_Filters_on_Image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N9EhsG2HCqVv7RuEIbqxeO-5LaO7IxMC

#Image Filtering Techniques
## Filter in DIP
Image Filtering is a step during image preprocessing.
When it comes to detecting edges and contours, noise gives a great impact on the accuracy of detection.
Therefore removing noises and controlling the intensity of the pixel is necessary.

* Image filtering is done to remove noise and any undesired features from an image, creating a better and enhanced version of that image.

>There are two types of filters that exist: linear and non-linear.
- Linear Filter: Mean, Laplacian
- Non-Linear Filter: Median, GaussianBlur

## Applying Filters to Image using Open CV
1. Laplacian Operator
2. Sobel Operator
3. Median
4. Canny
5. Guassian
6. Prewitt Operator
7. Robinson Compass Masks
8. Krisch Compass Masks

## Operator/ Filters -OverView
### Prewitt Operator:
>> Prewitt operator is used for detecting edges horizontally and vertically.

### Sobel Operator:
>> The sobel operator is very similar to Prewitt operator. It is also a derivate mask and is used for edge detection. It also calculates edges in both horizontal and vertical direction.

### Robinson Compass Masks:
>> This operator is also known as direction mask. In this operator we take one mask and rotate it in all the 8 compass major directions to calculate edges of each direction.

### Kirsch Compass Masks:
>> Kirsch Compass Mask is also a derivative mask which is used for finding edges. Kirsch mask is also used for calculating edges in all the directions.

### Laplacian Operator:
>>Laplacian Operator is also a derivative operator which is used to find edges in an image. Laplacian is a second order derivative mask. It can be further divided into positive laplacian and negative laplacian.

* All these masks find edges.
* Some find horizontally and vertically, some find in one direction only and some find in all the directions.
"""

# Commented out IPython magic to ensure Python compatibility.
#importing libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from google.colab import files
f"Open Cv verion:{cv.__version__} AND Numpy Version:{np.__version__}"

#import from local drive
uploaded = files.upload()
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

"""## Reading colored Image"""

def plotIMG(img_source):
  plt.imshow(img_source)

img= cv.imread("profile-pic.png",cv.IMREAD_COLOR)
plotIMG(img)

"""## Lets do some Effect:
1. Simple Blur
2. Median Blur
3. Guassian Blur
4. Billateral Filter
5. Laplacian
6. Sobel
7. Canny
"""

#1B
b_img = cv.blur(img,(10,10))
plotIMG(b_img)

#2B
b_img=cv.medianBlur(img,1)
plotIMG(b_img)

#3B
b_img=cv.GaussianBlur(img,(25,25),0)
plotIMG(b_img)

#4B
b_img=cv.bilateralFilter(img,41,62,62)
plotIMG(b_img)

#5B
b_img=cv.Canny(img,60,100)
plotIMG(b_img)

#laplacian
b_img=cv.Laplacian(img,cv.CV_64F,3)
plotIMG(b_img)

#Sobel
b_img=cv.Sobel(img,cv.CV_16U,1,0,ksize=5) # X Sobel
# b_img= cv.Sobel(img,cv.CV_64F,0,1,5)# Y Sobel
# dest=cv.convertScaleAbs(b_img)
plotIMG(b_img)