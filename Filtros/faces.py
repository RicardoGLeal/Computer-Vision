import numpy as np
import cv2

def run():
	cap = cv2.VideoCapture(0)
	print('Iniciando camara...')
	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

	#si no se detectó ninguna camara..
	if not cap.isOpened():
		print("No se encontro ninguna cámara")
		exit()

	while True:
		ret,frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#Se realiza la busqueda de caras en el video tomando escala 1.3 del clasficador
		# y 5 neighbors juntos para saber si es una cara
		faces = faceClassif.detectMultiScale(gray,1.3, 5)

		#Se generan los rectangulos alrededor de la cara con color verde y ancho dos
		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

		#Se muestra el video en pantalla
		cv2.imshow('frame',frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()