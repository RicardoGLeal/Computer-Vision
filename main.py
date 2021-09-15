import cv2
from os import system, name
#import colores.py
#import bw.py
#import contornos.py
#import figuras.py

def main():
    while(True):
        print('Que quieres hacer?: \n')
        print('[1] Identificar colores \n') 
        print('[2] Ver camara blanco y negro \n') 
        print('[3] Identificar contornos \n') 
        print('[4] Identificar figuras \n') 
        print('Cualquier otra tecla para salir :( \n') 
        seleccion = input()
        
        if seleccion == '1':
            print('Ejecutando colores.py')
        elif seleccion == '2':
            print('Ejecutando bw.py')
        elif seleccion == '3':
            print('Ejecutando contornos')
        elif seleccion == '4':
            print('Ejectuando figuras.py')
        else:
            break
        _ = system('cls')
    return 1

main()