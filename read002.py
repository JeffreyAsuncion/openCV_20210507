# reading and viewing videos

import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg') # 2300 x 1600 : too big for screen

# cv.imshow('Cat', img)

# Reading Videos
# capture = cv.VideoCapture(0)  # 0 is for webcam, 1 aux cam, 2 so on...
capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    isTrue, frame = capture.read() # reads frame for frame, and boolean (success or not)
    cv.imshow('Video', frame)

    # breaks at the end of the video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capture pointer
capture.release()
cv.destroyAllWindows()
