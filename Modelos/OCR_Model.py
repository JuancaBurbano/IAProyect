# Librerias

import cv2
import pytesseract as tess
from PIL import Image
import os

# Funcion
def text(image_path):
    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    image = cv2.imread(image_path)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texto = tess.image_to_string(gris)
    print(texto)

    output_folder = r"Data/Texto/"
    output_file = os.path.join(output_folder, 'texto.txt')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(texto)

# Llamar la función
image_path = "Data/Capturas/Img.jpg"
text(image_path)


