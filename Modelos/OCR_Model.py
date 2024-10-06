# Librerias

import cv2
import pytesseract as tess
from PIL import Image
import os

# Función
def text(image_path):
    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    image = cv2.imread(image_path)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, thresholded = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow('Otsu', thresholded)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()  
    
    dist = cv2.distanceTransform(thresholded, cv2.DIST_L2, 5)
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    dist = (dist * 255).astype('uint8') 

    cv2.imshow('Dist', dist)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    _, dist1 = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('Dist Otsu', dist1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    texto = tess.image_to_string(dist1)
    print(texto)

    # Guardar el texto en un archivo
    output_folder = r"Data/Texto/"
    os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta si no existe
    output_file = os.path.join(output_folder, 'texto.txt')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(texto)

# Llamar la función
image_path = "Data/Capturas/Img.jpg"
text(image_path)
   


