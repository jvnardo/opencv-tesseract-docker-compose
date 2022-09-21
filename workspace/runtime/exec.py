import cv2
import pytesseract
import os
import glob


imagems = (glob.glob('*jpg'))
#imagems = (os.listdir ())
for imagem in imagems:
	img = cv2.imread(imagem)
	resultado = pytesseract.image_to_string(img)
	print(resultado)
#print (imagems)
