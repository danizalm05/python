import cv2
import numpy as np

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "cards.jpg"
path = BASE_FOLDER +  mimg

img  = cv2.imread(path)


width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188],[154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
print(matrix.shape)#3,3
print(matrix )
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)