import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# canny = cv.Canny(blur,125,175)
# cv.imshow('Cannay edges',canny)

ret,thresh = cv.threshold(gray,125,255,type=cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

blank = np.zeros(img.shape,dtype='uint8')
contours,hierarchis = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found")

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Draw',blank)

cv.waitKey(0)