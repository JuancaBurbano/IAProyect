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
    
    # Buscamos la sección de definiciones. En Merriam-Webster, las definiciones están en un div con clase 'vg'
    definitions_section = soup.find_all('span', {'class': 'dtText'})
    
    # Si no encontramos definiciones, devolvemos un mensaje de error
    if not definitions_section:
        print(f"No se encontró la definición para '{word}'.")
        return None
    
    # Extraemos todas las definiciones, limpiando caracteres innecesarios como ":"
    definitions = [definition.get_text(strip=True).lstrip(":") for definition in definitions_section]
    
    return definitions

# Función para manejar la entrada del usuario y obtener definiciones para múltiples palabras
def main():
    while True:
        # Solicitar una o más palabras separadas por comas
        user_input = input("Introduce una palabra o varias (separadas por comas), o 'salir' para terminar: ").strip()
        
        if user_input.lower() == 'salir':
            print("Programa terminado.")
            break
        
        # Separar palabras si hay más de una
        words = [word.strip() for word in user_input.split(',')]
        
        for word in words:
            # Llamamos a la función de scraping para cada palabra
            definitions = scrape_definition(word)
            
            if definitions:
                print(f"\nDefiniciones para '{word}':")
                for i, definition in enumerate(definitions, 1):
                    print(f"{i}. {definition}")
            else:
                print(f"No se encontró la definición para '{word}'.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
