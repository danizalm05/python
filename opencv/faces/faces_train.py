"""
Face   face recog train  2.49 3:11
face_train.py
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o

https://github.com/jasmcaus/opencv-course/tree/master/Section%20%233%20-%20Faces

"""
import os
import cv2 as cv
import numpy as np

#people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'C:/Users/rockman/Pictures/Saved Pictures/Faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
people =[]
for i in os.listdir(DIR):
    people.append(i)
print(people)

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)# Path for  dir of each person

        label = people.index(person)# each person will  have index number 0,1...
        #print(path,label)
        # path = C:/Users/rockman/Pictures/Saved Pictures/Faces/train\Ben Afflek  label = 0
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            #print (img_path)
            # C:/Users/rockman/Pictures/Saved Pictures/Faces/train\Ben Afflek\1.jpg
            # ....
            # C:/Users/rockman/Pictures/Saved Pictures/Faces/train\Ben Afflek\14.jpg
            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)# add this face
                labels.append(label)# Add  the  label of the face


create_train()

print(f' length of features list = {len(features)}  ')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

print('Start Training   ...')
# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

print('saving results  ...')

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)