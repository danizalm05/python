"""
Contours and Shape detection
Murtaza's Workshop - Robotics and AI   1:15:37 1:30
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """

import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#  --   getContours ----    #


def getContours(img):
  contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  i = 0
  for cnt in contours:
       i += 1
       area = cv2.contourArea(cnt)

       if area > 500:
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
        peri = cv2.arcLength(cnt, True)# closed shapes ==> True
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # closed shapes ==> True
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        print(i, ' : ', area,' peri =  ',peri,'len(approx) = ', objCor)
        print(approx) #approx ===> corner   points. 3 is trinagle 4 rect and >4  circle
        print('cv2.boundingRect(approx) =', cv2.boundingRect(approx))

        if objCor == 3:
             objectType = "Tri"
        elif objCor == 4:
             aspRatio = w / float(h)
             if aspRatio > 0.98 and aspRatio < 1.03:
                 objectType = "Square"
             else:
                 objectType = "Rectangle"
        elif objCor > 4:
            objectType = "Circles"
        else:
            objectType = "None"

        cv2.rectangle(imgContour, (x, y), (x+w, y+h),(0, 220, 0),2)
        cv2.putText(imgContour, objectType,
            (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
            (0, 0, 0), 2)
#############

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
img_name = "shapes.png"
path = BASE_FOLDER + img_name

img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur, 50, 50)# Edge  detect
getContours(imgCanny)

##  Display   results
scale = 0.5
img_array = (  [img, imgGray, imgBlur  ],   [imgCanny, imgContour, img]  )
imgStack = stackImages(scale, img_array)
cv2.imshow("ImageStack",imgStack)

cv2.imshow("imgContour", imgContour)



cv2.waitKey(0)