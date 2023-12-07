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

