# How to switch between color spaces (greyscale, RGB, HSV, LAB, YCrCb) in openCV

# Note : CANNOT convert Grayscale to HSV directly
# you have to grayscale to BGR and then BRG to HSV 

import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()


# BGR(default) to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RBG', rgb)

plt.imshow(rgb)
plt.show()

# Note : CANNOT convert Grayscale to HSV directly
# you have to grayscale to BGR and then BRG to HSV 

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)



cv.waitKey(0)