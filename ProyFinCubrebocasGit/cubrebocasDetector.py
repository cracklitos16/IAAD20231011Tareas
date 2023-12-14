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
