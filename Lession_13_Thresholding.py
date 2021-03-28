import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/cat.png')
img = cv.resize(img,(640,480))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Simple Theresholding 
thereshold, theresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',theresh)

# Simple Threshold Inverse
thereshold,theresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse',theresh_inv)

# Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
cv.imshow("Adaptive Thresh Mean",adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,9)
cv.imshow("Adaptive Thresh Gaussian",adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow("Adaptive Thresh Gaussian Inverse",adaptive_thresh)

cv.waitKey(0)