"""
Face   Recogniation  2.49 3:11
face_train.py
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o

https://github.com/jasmcaus/opencv-course/tree/master/Section%20%233%20-%20Faces

"""
import os
import cv2 as cv
import numpy as np



DIR = r'C:/Users/rockman/Pictures/Saved Pictures/Faces/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people =[]
for i in os.listdir(DIR):
    people.append(i)
print(people)
#people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/Faces/val/'
NAME = 'mindy_kaling/'
mimg = "4.jpg"
path = BASE_FOLDER + NAME +mimg
print(path)

img = cv.imread(path)
cv.imshow('Original', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person gray', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX,
                    1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Person', img)

cv.waitKey(0)