import cv2

def run(): 
    capture = cv2.VideoCapture(0)
    print('Iniciando camara...')
    while (True):
    
        (ret, frame) = capture.read()
    
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)
    
    
        cv2.imshow('video bw', blackAndWhiteFrame)
        
    
        if cv2.waitKey(1) == ord("q"):
            break
    
    capture.release()
    cv2.destroyAllWindows() 
