# Contours and Edges are different
# Best method is 1. blur, 2. canny, 3.contours 

import cv2 as cv
import numpy as np


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

# 1. convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# # OPTION #1
# # add a blur
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
# # 2. grab edges with canny detector
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# OPTION #2
# using threshold
# Threshold looks at img tries to binaryize it?
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


# 3. find contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)  # OPTION 2
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # OPTION 1
print(f"{len(contours)} contour(s) found!")


# Draw contours on the blank
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
