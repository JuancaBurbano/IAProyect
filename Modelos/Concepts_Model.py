import requests
from bs4 import BeautifulSoup

# Función para hacer scraping y obtener el significado de una palabra en inglés
def scrape_definition(word):
    # URL del diccionario Merriam-Webster
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    
    # Hacemos la solicitud a la página
    response = requests.get(url)
    
    # Verificamos que la página responda correctamente
    if response.status_code != 200:
        print(f"Error al acceder a la página. Código: {response.status_code}")
        return None
    
    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos la sección de definiciones. En Merriam-Webster, las definiciones están en un span con clase 'dtText'
    definitions_section = soup.find_all('span', {'class': 'dtText'})
    
    # Si no encontramos definiciones, devolvemos un mensaje de error
    if not definitions_section:
        print(f"No se encontró la definición para '{word}'.")
        return None
    
    # Extraemos todas las definiciones, limpiando caracteres innecesarios como ":"
    definitions = [definition.get_text(strip=True).lstrip(":") for definition in definitions_section]
    
    return definitions

# Función para leer la palabra desde un archivo de texto
def read_word_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Leer el contenido del archivo (asumimos que hay solo una palabra en el archivo)
        word = file.read().strip()
    return word

# Función principal que obtiene la palabra desde el archivo y luego busca su definición
def main():
    # Ruta del archivo de texto
    file_path = r'C:\Users\playc\Desktop\IA\Data\Texto\textoTrad.txt'
    
    # Leer la palabra desde el archivo
    word = read_word_from_file(file_path)
    
    # Llamamos a la función de scraping para la palabra leída
    definitions = scrape_definition(word)
    
    if definitions:
        print(f"\nDefiniciones para '{word}':")
        for i, definition in enumerate(definitions, 1):
            print(f"{i}. {definition}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
