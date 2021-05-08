# Rescale and Resize in OpenCV

import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg') # 2300 x 1600 : too big for screen
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):  #default scale=0.75
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos
# capture = cv.VideoCapture(0)  # 0 is for webcam, 1 aux cam, 2 so on...
capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    isTrue, frame = capture.read() # reads frame for frame, and boolean (success or not)
    
    frame_resized = rescaleFrame(frame)
    frame_resized_resized = rescaleFrame(frame, 0.50)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    cv.imshow('Video Resized Resized', frame_resized_resized)
    # breaks at the end of the video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capture pointer
capture.release()
cv.destroyAllWindows()
