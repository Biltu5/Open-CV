# Before run this file run 'Lession_16_Face_Reconization_Part_1.py' file
import numpy as np
import cv2 as cv 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Mahendra Sing Dhoni','Virat Koholi','Rohit Sharma']

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_reconizer = cv.face.LBPHFaceRecognizer_create()
face_reconizer.read('face_trained.yml')

# Load image to check detect face is right or wrong
img = cv.imread("E:/OpenCV/test/VK/V (3).jpg")
img = cv.resize(img,(500,400),interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Person',gray)

# Detect the face in Image 
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h,x:x+w]
    label,confidence = face_reconizer.predict(face_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,str(people[label]),(10,25),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)
cv.waitKey(0)