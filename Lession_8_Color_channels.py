import cv2 as cv
import numpy as np
img = cv.imread('Images/cat.png')

b,g,r = cv.split(img)

# Show split images
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

# Show shape to better understand 
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Marged split  images and get original image
marged = cv.merge([b,g,r])
cv.imshow('Marged Image',marged)

# Draw split images on a blank image
blank = np.zeros(img.shape[:2],dtype = 'uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue1',blue)
cv.imshow('Green1',green)
cv.imshow('Red1',red)

cv.waitKey(0)