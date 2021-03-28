import numpy as np
import cv2 as cvp

# read image
img = cv.imread('Images/cat.png')
img = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),interpolation=cv.INTER_CUBIC)

# Create a  blank image
blank = np.zeros(img.shape[:2],dtype='uint8')

# Create a mask
mask = cv.circle(blank.copy(),(280,150),130,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow('Masked',masked)
cv.waitKey(0)