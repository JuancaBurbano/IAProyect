import Levenshtein

def read_text_from_file(file_path):
    """Lee el texto de un archivo de texto"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def calculate_CAR(ocr_file_path, reference_text):
    """Calcula la métrica Character Accuracy Rate (CAR)"""
    
    # Leer el texto OCR desde el archivo
    ocr_text = read_text_from_file(ocr_file_path)

    # Obtener la distancia de Levenshtein (número de ediciones)
    levenshtein_distance = Levenshtein.distance(ocr_text, reference_text)

    # Longitud total del texto de referencia
    total_chars = len(reference_text)

    # Fórmula de CAR: (Total caracteres - errores) / Total caracteres
    car = (total_chars - levenshtein_distance) / total_chars
    
    return car

# Ruta del texto extraído
ocr_file_path = r"C:\Users\USUARIO\Desktop\IA Proyecto\IAProyect\Data\Texto\texto.txt"

# Pedir al usuario que ingrese el texto de referencia
reference_text = input("Ingresa el texto de referencia: ")

# Llamada a la función para calcular el CAR
car_score = calculate_CAR(ocr_file_path, reference_text)
print(f"CAR score: {car_score}")
