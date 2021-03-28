import cv2 as cv

img = cv.imread('Images/cat.png')

# resize 
img = cv.resize(img,(500,400),interpolation=cv.INTER_AREA)

# Converting to Gray Scale
gray = cv.cvtColor(img,code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur [Removing noice from an image]
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# edge cascade [The function finds edges in the input image and marks them in the output map
# edges using the Canny algorithm.The smallest value between threshold1 and threshold2 is used 
# for edge linking. The largest value is used to find initial segments of strong edges.]
canny = cv.Canny(img,125,175)
cv.imshow('Canny edges',canny)

# Eroding [The function erodes the source image using the specified structuring element that determines the
#   shape of a pixel neighborhood over which the minimum is taken]
eroded = cv.erode(img,(7,7),iterations=3)
cv.imshow('eroded',eroded)

# Croping
croped = img[50:200,200:400]
cv.imshow("resized",croped)

cv.waitKey(0)