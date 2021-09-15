import cv2

gaussVal = 3
capturaVideo = cv2.VideoCapture(0)


if not capturaVideo.isOpened():
    print("No se enconctró ninguna cámara")
    exit()

while True:

    tipo, camara = capturaVideo.read()
    gris = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gris,(gaussVal,gaussVal), 0)
    canny = cv2.Canny(gauss, 20, 100)

    cv2.imshow("En Vivo", canny)
    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()