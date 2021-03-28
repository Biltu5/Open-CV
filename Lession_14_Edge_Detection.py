import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.png')
img = cv.resize(img,(640,480))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian Method 
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel Method 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobal X',sobelx)
cv.imshow('Sobal Y',sobely)
cv.imshow('Combined Sobal',combined_sobel)

# Canney Method 
canny = cv.Canny(gray,150,175)
cv.imshow('Cannay',canny)

cv.waitKey(0)