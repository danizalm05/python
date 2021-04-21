"""
Face  detection  2:35 2.49
face_detect.py
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/tree/master/Section%20%233%20-%20Faces
   """
import cv2 as cv
import numpy as np

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
#mimg = "lady.JPG"
mimg = "group 1.jpg"#group 2.jpg"
path = BASE_FOLDER + mimg

img = cv.imread(path)




gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=  1.1, minNeighbors= 1 )
# Change the  values of 'scaleFactor' or 'minNeighbors' above to get better  results
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in  faces_rect:
    print (x, y, w, h)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness = 2)

cv.imshow('detect', img)

cv.waitKey(0)