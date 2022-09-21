#opencv
import cv2
import pytesseract
import os
import glob,os.path


imagems = (glob.glob('imagens/*'))
#imagems = (os.listdir ())
for imagem in imagems:
	img = cv2.imread(imagem)
	resultado = pytesseract.image_to_string(img)
	print(resultado)
#print (imagems)
