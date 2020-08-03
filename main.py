import cv2
import numpy as np
import pyautogui as gui

cap = cv2.VideoCapture(0)
lower_white = np.array([0, 0, 0])
upper_white = np.array([0, 0, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_white, upper_white)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for each_contour in contours: #loop through all contours
        area = cv2.contourArea(each_contour)
        if area > 10000: #area fixing
           # cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
           x,y,w,h = cv2.boundingRect(each_contour) #creating rectangle
           cv2.rectangle(frame, (x,y), (x + w, y + h), (120,25, 100), 2) #purple color boarder
           if y < prev_y:
               gui.press('down')

           prev_y = y

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('a'):  #window will stop if key 'a'is pressed
        break

cap.release()
cv2.destroyAllWindows()

