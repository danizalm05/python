"""
Fourier Transform – OpenCV 3.4 with python 3 Tutorial 35
https://www.youtube.com/watch?v=cLHAUhGkzwQ
https://pysource.com/2018/08/04/fourier-transform-opencv-3-4-with-python-3-tutorial-35/

 """


import cv2
import numpy as np


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/fourier/'
img_name = "horizontal_lines.jpg"
path = BASE_FOLDER + img_name
#print(path)

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Stacked Images", img)
f = np.fft.fft2(img)
cv2.waitKey(0)
cv2.destroyAllWindows()