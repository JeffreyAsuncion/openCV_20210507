import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

# keyboard binding function (Note key press on image to exit)
cv.waitKey(0)