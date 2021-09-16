import cv2

def run():
    #Variable para la matriz a usar en el blur gaussiano
    gaussVal = 3
    #Deteccion de la camara predeterminada
    capturaVideo = cv2.VideoCapture(0)
    print('Iniciando camara...')
    #En caso de no detectar ninguna cámara
    if not capturaVideo.isOpened():
        print("No se enconctró ninguna cámara")
        exit()

    #Mientras la cámara está abierta
    while True:
        #Se lee la imagen de la camara
        tipo, camara = capturaVideo.read()
        #Se convierte a escala de grises
        gris = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)
        #Se hace un blur gaussiano para eliminar ruido
        gauss = cv2.GaussianBlur(gris,(gaussVal,gaussVal), 0)
        #Se aplica la convolucion de Canny para detectar los bordes
        canny = cv2.Canny(gauss, 20, 100)
        #Se muestra la imagen
        cv2.imshow("En Vivo", canny)
        #Condicion para cerrar la ventana
        if cv2.waitKey(1) == ord("q"):
            break

    #Se detiene la captura de la cámara y se destruyen las ventanas
    capturaVideo.release()
    cv2.destroyAllWindows()