import numpy as np
import cv2

def run():
    capturaVideo = cv2.VideoCapture(0)
    print('Iniciando camara...')
    #si no se detectó ninguna camara..
    if not capturaVideo.isOpened():
        print("No se enconctró ninguna cámara")
        exit()

    #mientras la camara esté abierta..
    while capturaVideo.isOpened():
        tipo, camara = capturaVideo.read()
        
        #se obtienen los pixeles rgb y los convierte en hsv.
        hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)
        
        #se definen los colores que se quieren extraer de la imagen.
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(camara, camara, mask=mask)

        cv2.imshow("En Vivo", result)

        if cv2.waitKey(1) == ord("q"):
            break

    capturaVideo.release()
    cv2.destroyAllWindows()