import cv2
import numpy as np
from os import system, name
import Filtros.Bnw as bnw
import Filtros.bordes as borders
import Filtros.colores as colors
import Filtros.faces as faces

def main():
    while(True):
        print('Que quieres hacer?: \n')
        print('[1] Identificar colores \n') 
        print('[2] Ver camara blanco y negro \n') 
        print('[3] Identificar contornos \n') 
        print('[4] Reconocimiento facial \n') 
        print('Cualquier otra tecla para salir :( \n') 
        seleccion = input()
        
        if seleccion == '2':
            bnw.run()
        elif seleccion == '3':
            borders.run()
        elif seleccion == '1':
            colors.run()
        elif seleccion == '4':
            faces.run()
        else:
            break
        _ = system('cls')
    return 1

main()