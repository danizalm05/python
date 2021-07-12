'''
Display tame of images
example:
  import ImageTable
  
  scale = 0.6
  img_array = ([img, img1, img2], [img3 , img4 , img5])
  imgStack = ImageTable.stackImages(scale, img_array)
  cv2.imshow("original", imgStack)
'''


import cv2
import numpy as np
def empty(a):
    pass
def stackImages(scale,imgArray,titleArray =[]):
    rows = len(imgArray)
    cols = len(imgArray[0])

    for i in range(0, rows):
        for j in range(0, cols):
            #print(i,j," : ", titleArray[i][j])
            px, py, w, h = 8, 42, 675, 55



            # Draw black background rectangle
            cv2.rectangle( imgArray[i][j], (0, 0), (700, 45), (0, 0, 0), -1)
            title = "[" + str(i) + ":" + str(j) + "] " + titleArray[i][j]
            print(title)

            cv2.putText(imgArray[i][j], title, (px, py),  # position for writing
                cv2.FONT_HERSHEY_SIMPLEX, 2,  # font size
                (255,  0, 255),  # font color
                4)  # font stroke
            #cv2.imshow(title, imgArray[i][j])
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
