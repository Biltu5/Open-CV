import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.png')
img = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),interpolation=cv.INTER_CUBIC)
cv.imshow('Cat',img)

# Create a blank image
blank = np.zeros(img.shape[:2],dtype='uint8')

# Create a rectangle
rectangle = cv.rectangle(blank.copy(),(150,50),(350,250),255,-1)
cv.imshow('Rectangle',rectangle)

# Create a circle
circle = cv.circle(blank.copy(),(250,150),115,255,-1)
cv.imshow('circle',circle)

# Bitwise AND [Intersection]
bitwise_AND = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise And',bitwise_AND)

# Bitwise OR [Union]
bitwise_OR = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_OR)

# Bitwise XOR [Non-intersectio region]
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('Biwtwise XOR',bitwise_XOR)

# Bitwise NOT [complement of the image]
bitwise_NOT = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT',bitwise_NOT) 

cv.waitKey(0)