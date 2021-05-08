# Reading images 

import cv2 as cv

img = cv.imread('Photos/cat.jpg') # 640 x 427
# img = cv.imread('Photos/cat_large.jpg') # 2300 x 1600 : too big for screen

cv.imshow('Cat', img)

# keyboard binding function (Note key press on image to exit)
cv.waitKey(0)