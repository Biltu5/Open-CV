import cv2 as cv
# read image 
img = cv.imread('Images/cat.png')
cv.imshow('Cat',img)
cv.waitKey(0)

#read video
capture = cv.VideoCapture('Videoes/dog.mp4')
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()