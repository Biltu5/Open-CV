import cv2 as cv
import numpy as np 

img = cv.imread('Images/cat.png')

# Translation
def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimentions)

translate = translate(img,100,100)
cv.imshow('Translated',translate)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    dimention = (width,height)
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    return cv.warpAffine(img,rotMat,dimention)

rotated = rotate(img,45)
cv.imshow('Rotated',rotated)

# Resize 
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flipping
flip = cv.flip(img,0)
cv.imshow('Flip',flip)

# Crop
cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)