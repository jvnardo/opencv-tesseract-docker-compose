#opencv
import cv2
import pytesseract

img = cv2.imread("image.jpg")
resultado = pytesseract.image_to_string(img)
print(resultado)