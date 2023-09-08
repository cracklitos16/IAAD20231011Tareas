import numpy as np
import cv2 as cv
import math 

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
#i = 0
while True:
    ret, frame = cap.read()
    #i=i+1
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        frame = cv.rectangle(frame, (x+100,y+150), (x+w-10, y+h-100), (255, 0, 0), 4)
        #frame = cv.circle(frame, (x+int(w/2), y+int(h/2)), 60, (0,0,255),2 )
    cv.imshow('rostros', frame)
    #cv.imwrite('ruta'+str(i)+'.jpg',frame)
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()