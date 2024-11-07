import requests
from bs4 import BeautifulSoup
import os

# Función para hacer scraping y obtener el significado de una palabra en inglés
def scrape_definition(word):
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error al acceder a la página. Código: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    definitions_section = soup.find_all('span', {'class': 'dtText'})
    
    if not definitions_section:
        print(f"No se encontró la definición para '{word}'.")
        return None
    
    definitions = [definition.get_text(strip=True).lstrip(":") for definition in definitions_section]
    return definitions

# Función para leer la palabra desde un archivo de texto
def read_word_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        word = file.read().strip()
    return word

# Función principal
def main():
    file_path = r"C:\Users\USUARIO\Desktop\IA Proyecto\IAProyect\Data\\Texto\textoTrad.txt"
    word = read_word_from_file(file_path)

    # Verificar si es una sola palabra o una frase
    word_count = len(word.split())
    
    # Llamamos a la función de scraping para la palabra leída
    definitions = scrape_definition(word)

    if definitions:
        if word_count == 1:
            print(f"\nTraducción y concepto para '{word}':")
            # Mostrar la traducción (simulada) y el concepto
            print(f"Traducción: [Traducción simulada de '{word}']")  # Aquí puedes incluir la lógica para obtener la traducción
            print(f"Concepto: {definitions[0]}")  # Mostrar la primera definición como concepto
        else:
            print(f"\nTraducción de la frase '{word}':")
            # Mostrar solo la traducción (simulada)
            print(f"Traducción: [Traducción simulada de '{word}']")  # Aquí puedes incluir la lógica para obtener la traducción

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

