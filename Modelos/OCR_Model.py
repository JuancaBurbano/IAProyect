# Librerías
import cv2  
import pytesseract as tess  
from PIL import Image  
import os  

# Función para procesar la imagen y extraer texto usando OCR
def text(image_path):
    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # Lee la imagen desde la ruta especificada
    image = cv2.imread(image_path)
    
    # Convierte la imagen a escala de grises (BGR a Gray)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica umbralización Otsu y binarización invertida para obtener áreas relevantes de la imagen
    _, thresholded = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Muestra la imagen umbralizada (binaria invertida)
    cv2.imshow('Otsu', thresholded)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  # Cierra la ventana de la imagen
    
    # Aplica la transformación de distancia para resaltar áreas importantes en la imagen
    dist = cv2.distanceTransform(thresholded, cv2.DIST_L2, 5)
    
    # Normaliza los valores de la transformación de distancia a un rango de 0 a 1, y luego escala a 0-255
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    dist = (dist * 255).astype('uint8')  # Convierte a una imagen de 8 bits para facilitar el procesamiento
    
    # Muestra la imagen con la transformación de distancia
    cv2.imshow('Dist', dist)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  # Cierra la ventana de la imagen
    
    # Aplica umbralización Otsu nuevamente sobre la imagen transformada
    _, dist1 = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Muestra la imagen final después de la segunda umbralización
    cv2.imshow('Dist Otsu', dist1)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  # Cierra la ventana de la imagen
    
    # Utiliza Tesseract para extraer el texto de la imagen procesada
    texto = tess.image_to_string(dist1)
    
    # Imprime el texto extraído en la consola
    print(texto)

    #Guarda el archivp
    output_folder = r"Data/Texto/"
    
    # Crear la carpeta si no existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Define la ruta del archivo donde se guardará el texto extraído
    output_file = os.path.join(output_folder, 'texto.txt')
    
    # Abre el archivo en modo escritura y lo guarda en formato UTF-8
    with open(output_file, 'w', encoding='utf-8') as f:
        # Escribe el texto extraído en el archivo
        f.write(texto)

# Llamada a la función con la ruta de la imagen a procesar
image_path = "Data/Capturas/Img.jpg"
text(image_path)

   


