import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/cat.png')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Gray Scale Histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

# Show Gray Scale Histogram
plt.figure('GrayScale Histogram ')
plt.xlabel('Bins')
plt.ylabel('of Pixel')
plt.plot(gray_hist)
plt.xlim([0,256])  # Get or set the x limits of the current axes.
plt.show()

# Create a blank Image 
blank = np.zeros(img.shape[:2],dtype='uint8')

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),220,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
gary_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure('GrayScale Histogram 2 ')
plt.xlabel('Bins')
plt.ylabel('of Pixel')
plt.plot(gray_hist)
plt.xlim([0,256])  # Get or set the x limits of the current axes.
plt.show()

cv.imshow('Mask',mask)

# Color Histogram 
mask1 = cv.bitwise_and(img,img,mask=circle)
color =('b','g','r')
plt.figure('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('of Pixel')
for i,col in enumerate(color):
    hist1 = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist1,color=col)
    plt.xlim([0,256])
plt.show()
cv.imshow('Mask2',mask1)
cv.waitKey(0)