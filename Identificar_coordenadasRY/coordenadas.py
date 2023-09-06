import cv2 as cv
import numpy as np

# Abre la cámara. Si tienes varias cámaras, puedes cambiar el índice.
cap = cv.VideoCapture('Users\carlo\Documents\TEC\Semestre 8\Inteligencia Artificial\Identificar_coordenadasRY\tr.png')

while True:
    ret, img = cap.read()
    img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img3 = cv.cvtColor(img2, cv.COLOR_RGB2HSV)
    
    umbralbajo = (200, 0, 0)
    umbralalto = (255, 100, 100)

    mascara = cv.inRange(img3, umbralbajo, umbralalto)

    resultado = cv.bitwise_and(img, img, mask=mascara)
    
    cv.imshow('resultado', resultado)
    cv.imshow('mascara', mascara)
    cv.imshow('img', img)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

# Libera la cámara y destruye todas las ventanas al salir del bucle
cap.release()
cv.destroyAllWindows()
