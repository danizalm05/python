 
"""
  
AI Virtual Painter | OpenCV Python | Computer Vision

Murtaza's Workshop
https://www.computervision.zone/courses/ai-virtual-painter/lesson/ai-virtual-painter-lesson/  
   
29:00

"""
import cv2
import numpy as np
import time
import os
import HandTrackingModuleN as htm

camera_number = 0
folderPath = "pic" # name of picture directory
myList = os.listdir(folderPath)

#load header picture in a list
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(camera_number)
(frame_width, frame_hight) = (1280,720)
cap.set(3, frame_width)
cap.set(4, frame_hight)

detector = htm.handDetector(detectionCon=0.65,maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((frame_hight, frame_width, 3), np.uint8)
while True:

    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
       #print(lmList) #[id, x, y]
       # tip of index and middle fingers
       x1, y1 = lmList[8][1:]# x,y of id=8 index finger (move cursor)
       x2, y2 = lmList[12][1:]# x,y of id=8 middle finger (move cursor + left button )
       print(x1, y1,lmList[8])

       # 3. Check which fingers are up
       fingers = detector.fingersUp()


    img[0:125, 0:1280] = header
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break