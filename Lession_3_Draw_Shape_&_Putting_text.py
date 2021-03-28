import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500,500,3),dtype='uint8')

# Paint the image with certain colour
blank[:] = (0,255,0)
cv.imshow('Blank',blank)

# Paint a part of the image
blank[200:300,300:400] =(0,0,255)
cv.imshow("Blank",blank)

# Draw a Rectangle
cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=2)
cv.imshow('Blank',blank)

# draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),radius=40,color=(0,0,255),thickness=2)
cv.imshow('Blank',blank)

# Draw  a line
cv.line(blank,(20,50),(230,180),(255,0,0),thickness=3)
cv.imshow('Blank',blank)

# Write text on an image
cv.putText(blank,"Hi,I am Nayak",(50,355),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(255,255,0),thickness=3)
cv.imshow('Blank',blank)

cv.waitKey(0)