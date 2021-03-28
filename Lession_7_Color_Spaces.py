import cv2 as cv
img = cv.imread('Images/cat.png')
#cv.imshow('Cat',img)

# BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# grayscale to BGR
bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow('BGR',bgr)

# bgr to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

# bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('Hsv',hsv)

# bgr to rgb
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

cv.waitKey(0)