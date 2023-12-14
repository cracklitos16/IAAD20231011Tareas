# Proyecto Final: 2-. Generar un DataSet y haarcascade de caras con cubre bocas

## Por: Calderón Piña Carlos Michell

### Puntos a evaluar

* Herramientas para generar el DataSet.
  
* Proceso de creación del DataSet.
  
* Ajusten con el XML generado.
  
* Calidad del XML.

Entonces inicialmente vamos a crear el DataSet, para ello vamos a hacer uso de las librerías de openCV, y además de esto enseguida se mostrará el código con el cual se realizaron las capturas de las imágenes tanto positivas como negativas que fueron usadas para crear el XML.

```Python
import cv2 as cv

cap = cv.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()
    frame = cv.rectangle(frame, (100,100), (400,400), (0,255,0), 2)
    cara = frame[100:400, 100:400] 
    frame3 = cv.resize(cara, (200,200))
    cv.imshow ('rostros', frame)
    cv.imshow('resize', frame3)
    cv.imshow ('cara', cara)

    k = cv.waitKey(1)
    if k == ord('s'):
        i=i+1
        cv.imwrite('C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin2Cubrebocas/ConCubrebocasPositivas/Positiva'+str(i)+'.jpg', frame3)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

```

Como se puede observar creamos un recuadro en el cual se le dan los valores de alto y ancho, seguido de esto hacemos otro frame donde nos encuadre las caras, claro esto es opcional, sin embargo, al tener de una mejor manera definida que es lo que vamos a capturar nos beneficia para tener un buen DataSet. Es importante también mencionar el uso del resize, este es únicamente para cambiar el tamaño de la captura, y así poder tener un DataSet un tanto ligero.

Al igual que el código anterior se usó para la captura de las fotos negativas, únicamente en ese código se cambió el nombre y con la diferencia de que en dichas fotos no se usó cubrebocas, solo se usó cubrebocas para la creación de las fotos positivas.

Importante saber: Una buena observación que hago al desarrollar esto es que al menos yo cometí el error de tener más fotos positivas que negativas, en ese caso, lo que hice fue tener un DataSet de 1000 fotos con 10 tipos de cubrebocas de colores diferentes (Las cuales fueron las positivas), y tan solo 530 fotos negativas... Esto afecto mucho y retraso el desarrollo ya que al tratar de generar el XML con la herramienta cascade trainer gui, nos daba error, y esto nos podría traer problemas de falsos positivos.

Seguido de esto es importante que dependiendo el tamaño de DataSet será la precisión del detector, y menor será el sesgo. en fin, a continuación, se mostrará el código con el que se realizó el detector, es importante mencionar que se tenía como idea que también detectara el rostro sin que tuviera nada, precisamente para que cuando si lo hubiera también lo detectara.

```Python
import cv2 as cv

# rostro_cascade = 'C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin2Cubrebocas/haarcascade_frontalface_alt.xml' 

rostro = cv.CascadeClassifier('C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin2Cubrebocas/DataSet/classifier/cascade.xml')
cap = cv.VideoCapture(0)
i=0
# font = cv.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    i=i+1
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=30, minSize=(80, 80))
    for (x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        cv.putText(frame, 'Rostro Con cubrebocas', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv.imshow('rostros', frame)
#   for (x, y, w, h) in rostros_totales:
#     frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
#     cv.putText(frame, 'Rostro Sin Cubrebocas', (x, y), font, 0.7, (0, 0, 255), 2)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

```

Es realmente sencillo en comparación a la realización, producción y procesamiento de las fotos del DataSet.
Si bien específicamente en el código solo se jugó un poco con el seteo de los datos del rostro en rostro.detectMultiScale para que funcione lo mejor posible.

__Aquí un ejemplo de cómo se ve con una persona:__

![yo con cubrebocas](rostromio.png)

__Aquí un ejemplo de cómo se ve con dos personas:__

![yo con cubrebocas](evidenciacubre.png)

Y así es como se ve ya funcionando.
