
import Levenshtein

def read_text_from_file(file_path):
    """Lee el texto de un archivo de texto"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def calculate_WAR(ocr_file_path, reference_text):
    """Calcula la métrica Word Accuracy Rate (WAR)"""
    
    # Leer el texto OCR desde el archivo
    ocr_text = read_text_from_file(ocr_file_path)

    # Dividir ambos textos en listas de palabras
    ocr_words = ocr_text.split()
    reference_words = reference_text.split()

    # Obtener la distancia de Levenshtein entre los textos
    levenshtein_distance = Levenshtein.distance(' '.join(ocr_words), ' '.join(reference_words))

    # Número total de palabras en el texto de referencia
    total_words = len(reference_words)

    # Fórmula de WAR: (Total palabras - errores) / Total palabras
    war = (total_words - levenshtein_distance) / total_words

    return war

# Ruta del texto extraído
ocr_file_path = r"C:\Users\USUARIO\Desktop\IA Proyecto\IAProyect\Data\Texto\texto.txt"

# Pedir al usuario que ingrese el texto de referencia
reference_text = input("Ingresa el texto de referencia: ")

# Llamada a la función para calcular el WAR
war_score = calculate_WAR(ocr_file_path, reference_text)
print(f"WAR score: {war_score}")

