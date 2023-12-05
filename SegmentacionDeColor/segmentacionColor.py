import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/Unidad 1/SegmentacionDeColor/tr.png', 1)

img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img2, cv.COLOR_RGB2HSV)

umbralBajo = (0, 85, 85)
umbralAlto = (5, 255, 255)
umbralBajoB = (20, 90, 90)
umbralAltoB = (35, 255, 255)


mascara1 = cv.inRange(img3, umbralBajo, umbralAlto)
mascara2 = cv.inRange(img3, umbralBajoB, umbralAltoB)

mascara = mascara1 + mascara2

resultado = cv.bitwise_and(img, img, mask=mascara)

cv.imshow('resultado', resultado)
cv.imshow('mascara', mascara)
cv.imshow('img',img)
cv.imshow('img2', img2)
cv.imshow('img3', img3)

cv.waitKey(0)
cv.destroyAllWindows()