import os
from PIL import Image 
# entrada
pasta = ''  # '.' = diretorio atual, '..' => anterior #PREENCHER DIRETORIO
extensoes = [] # deixe em branco para todos

# lê arquivos na pasta
arquivos = os.listdir(pasta)

# para cada arquivo na pasta
for i in arquivos:
    a = i.split('.')
    if(len(a)>1 and (a[1])==''): #PREENCHER TIPO
        Image1 = Image.open(''+i) #PREENCHER LOCAL DO ARQUIVO
        croppedIm = Image1.crop((0, 14, 200, 310)) 
        croppedIm.save("LOCAL ONDE SERA SALVO"+(i.split('.')[0])+"_CROP.TIPO","TIPO") #PREENCHER LOCAL ONDE SERA SALVO +"_CROP.TIPO","TIPO" 
		



	