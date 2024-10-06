#Librerias

import cv2

# Variables

cuadro = 100
ancho, alto = 640,480

# Captura de video

cap = cv2.VideoCapture(0)
cap.set(3,ancho)
cap.set(4,alto)

while True:
    ret, frame = cap.read()
    if ret == False:break
    cv2.putText(frame, 'Ubique aqui su texto', (158, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0),2)
    cv2.putText(frame, 'Ubique aqui su texto', (160, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.rectangle(frame, (cuadro, cuadro), (ancho - cuadro, alto - cuadro), (0, 0, 0), 2)
    x1, y1 = cuadro, cuadro
    ancho1, alto1 = (ancho - cuadro) - x1, (alto - cuadro) - y1
    x2, y2 = x1 + ancho1, y1 + alto1
    doc = frame[y1:y2, x1:x2]
    cv2.imwrite("Data/Capturas/Img.jpg", doc)


    cv2.imshow("BACK-END", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break

