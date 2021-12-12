import cv2
import numpy as np

cap = cv2.VideoCapture('take1.mpg')

while(1):

   
 # Take each frame
    _, frame = cap.read()

   
 # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
 # define range of red color in HSV
    lower_red = np.array([168,150,50]) #example value
    upper_red = np.array([180,255,255])

    
# Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

   
 # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
