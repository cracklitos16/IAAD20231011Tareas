import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/Identificar_coordenadasRY/tr.png', 1)
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img2, cv.COLOR_RGB2HSV)

umbralBajo = (0, 85, 85)
umbralAlto = (5, 255, 255)
umbralBajoB = (20, 90, 90)
umbralAltoB = (35, 255, 255)

mascara1 = cv.inRange(img3, umbralBajo, umbralAlto)
mascara2 = cv.inRange(img3, umbralBajoB, umbralAltoB)

resultado1 = cv.bitwise_and(img, img, mask=mascara1)
resultado2 = cv.bitwise_and(img, img, mask=mascara2)

# Encuentra las coordenadas del color rojo
coordenadas_rojo = cv.findNonZero(mascara1)

# Encuentra las coordenadas del color amarillo
coordenadas_amarillo = cv.findNonZero(mascara2)

if coordenadas_rojo is not None:
    print("Coordenadas del color rojo:")
    for coord in coordenadas_rojo:
        x, y = coord[0]  # Obtiene las coordenadas x e y del píxel
        print(f'Rojo: ({x}, {y})')

if coordenadas_amarillo is not None:
    print("\nCoordenadas del color amarillo:")
    for coord in coordenadas_amarillo:
        x, y = coord[0]  # Obtiene las coordenadas x e y del píxel
        print(f'Amarillo: ({x}, {y})')

cv.imshow('img',img)
cv.imshow('resultado rojo', resultado1)
cv.imshow('resultado amarillo', resultado2)
cv.imshow('mascara rojo', mascara1)
cv.imshow('mascara amarillo', mascara2)

cv.waitKey(0)
cv.destroyAllWindows()
