import cv2 as cv
def reScaleFrame(frame,scale=0.75):
    # Used for Image, Video, Live stream
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)

def changeRes(width,height):
    # Use this function only for live streams
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videoes/dog.mp4')

while True:
    isTrue,frame = capture.read()
    rescale_frame = reScaleFrame(frame,scale = 0.50)
    cv.imshow('Dog',rescale_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
