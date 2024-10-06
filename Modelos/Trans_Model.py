from googletrans import Translator
import os

def translate_text(text_path):
    translator = Translator()

    # Leer el contenido del archivo
    with open(text_path, 'r', encoding='utf-8') as f:
        text_to_translate = f.read().strip()  # Eliminar espacios en blanco

    # Contar las palabras en el texto
    word_count = len(text_to_translate.split())

    # Traducir el texto
    res = translator.translate(text_to_translate, src='es', dest='en')  # 'es' para español y 'en' para inglés
    translated_text = res.text

    # Si es una sola palabra, guardar en textoTrad.txt
    if word_count == 1:
        output_file = os.path.join(os.path.dirname(text_path), 'textoTrad.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        print(f"Traducción guardada en: {output_file}")
    else:
        # Si es una frase o más de una palabra, mostrar en pantalla
        print(f"Traducción de la frase:\n{translated_text}")

# Ruta del archivo de texto
text_path = r'C:\Users\playc\Desktop\IA\Data\Texto\texto.txt'

# Llamar a la función de traducción
translate_text(text_path)