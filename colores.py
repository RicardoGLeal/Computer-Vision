import numpy as np
import cv2

capturaVideo = cv2.VideoCapture(0)

#si no se detectó ninguna camara..
if not capturaVideo.isOpened():
    print("No se enconctró ninguna cámara")
    exit()

#mientras la camara esté abierta..
while capturaVideo.isOpened():
    tipo, camara = capturaVideo.read()
    
    cv2.imshow('Vivo', camara)
    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()