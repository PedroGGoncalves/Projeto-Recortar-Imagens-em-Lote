import os
from PIL import Image 
import time
import cv2
import numpy as np
# entrada
pasta = ''  # '.' = diretorio atual, '..' => anterior #PREENCHER DIRETORIO
extensoes = [] # deixe em branco para todos

# lê arquivos na pasta
arquivos = os.listdir(pasta)



cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
image = cv2.imread('') #PREENCHER DIRETORIO + ARQUIVO REFERENCIA
oriImage = image.copy()
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            
            for i in arquivos:
                a = i.split('.')
                if(len(a)>1 and (a[1])==''):#PREENCHER TIPO
                    image2 = cv2.imread(''+i) #PREENCHER LOCAL DO ARQUIVO
                    oriImage2 = image2.copy()
                    roi2 = oriImage2[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                    cv2.imwrite(""+(i.split('.')[0])+"_CROP.TIPO",roi2) #PREENCHER LOCAL ONDE SERA SALVO +"_CROP.TIPO" 

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
while True:
    
    i = image.copy()
    if not cropping:
        cv2.imshow("image", image)
    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (0,128,0), 2)
        cv2.imshow("image", i)
    keyCode = cv2.waitKey(1)

    if cv2.getWindowProperty("image", cv2.WND_PROP_VISIBLE) <1:
        break
# close all open windows
cv2.destroyAllWindows()
	