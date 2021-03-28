import cv2 as cv

img = cv.imread('Images/cat.png')

# Averaging Blur 
avg = cv.blur(img,(3,3))
cv.imshow('Blur',avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gussian Blur',gauss)

# Median Blur 
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

# Bilateral Blur
Bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',Bilateral)

# . bilateralFilter can reduce unwanted noise very well while keeping edges fairly sharp. 
#   However, it is
# . very slow compared to most filters.
cv.waitKey(0)