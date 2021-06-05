'''
#Image enhancements:
# Sometimes microscope images lack contrast, they appear to be washed out but they still contain information.
# (Show scratch assay and alloy images)
# We can mathematically process these images and make them look good,
#more importantly, get them ready for segmentation
Histogram equalization is a good way to stretch the histogram and thus
 improve the image.


https://www.youtube.com/watch?v=XfDkg3z3BCg
https://github.com/bnsreenu/python_for_microscopists/blob/master/027-image_processing_in_openCV_intro2-Thresholding.py

Alloy.jpg
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/Alloy.jpg
3:50
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

USER1 = "gilfm"
USER2 = "rockman"
BASE_FOLDER = 'C:/Users/'+ USER1 +'/Pictures/Saved Pictures/'
img_name = "Alloy.jpg"
path = BASE_FOLDER + img_name
img = cv2.imread(path,0)


equ = cv2.equalizeHist(img)
plt.hist(img.flat, bins=100, range=(0, 255))
plt.hist(equ.flat, bins=100, range=(0, 255))
plt.title('cv2.equalizeHist(img)')
plt.show()

cv2.imshow("Original Image", img)
cv2.imshow("Equalized", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()