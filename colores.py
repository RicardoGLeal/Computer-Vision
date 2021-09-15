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
    
    #se obtienen los pixeles rgb y los convierte en hsv.
    hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)

    cv2.imshow("En Vivo", hsv)

    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()