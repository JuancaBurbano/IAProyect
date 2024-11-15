import cv2
import pytesseract as tess
import os

def text(image_path):
    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    # Lee la imagen desde la ruta especificada
    image = cv2.imread(image_path)
    
    # Procesamiento de la imagen
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    dist = cv2.distanceTransform(thresholded, cv2.DIST_L2, 5)
    dist = (dist * 255).astype('uint8')
    _, dist1 = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Extraer texto
    texto = tess.image_to_string(dist1)
    
    # Guarda el texto en un archivo (opcional)
    output_folder = r"Data/Texto/"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'texto.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(texto)
    
    # Retorna el texto extraído
    return texto

# Ruta de la imagen para probar
image_path = '../IA/Data/Capturas/imagen_guardada.jpg'
resultado = text(image_path)
print("Texto extraído:", resultado)