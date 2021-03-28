import os
import cv2 as cv
import numpy as np 

# Folder names where train images are exits 
people = ['MSD','VK','RS']

# Full path of the directory where image folder are exits
dir = r'E:\OpenCV\train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(dir,person)
        label = people.index(person)

        for img in os.listdir(path):
            # Absoluate path of each image 
            img_path = os.path.join(path,img)
            # Read image using cv module
            img_array = cv.imread(img_path)
            # convert rgb image into gray scale 
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            # detect face from the image
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)

            for (x,y,w,h) in faces_rect:
                # Croped face from gray scale image
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'Length of the features {len(features)}')
print(f'Length of the Labels {len(labels)}')

features = np.array(features,dtype='object')
labels = np.array(labels)

face_reconizer = cv.face.LBPHFaceRecognizer_create()

# Train the reconizer on the features list and the label list
face_reconizer.train(features,labels)

# Save as .yml file for fast execution the program
face_reconizer.save('face_trained.yml')

# Save an array to a binary file in NumPy ``.npy`` format.
np.save('features.npy',features)
np.save('labels.npy',labels)