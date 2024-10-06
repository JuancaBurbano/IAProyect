from googletrans import Translator

def translate_text(text_path):
    translator = Translator()

    with open(text_path, 'r', encoding='utf-8') as f:
        text_to_translate = f.read()

    res = translator.translate(text_to_translate, src='es', dest='en')  # 'es' para español y 'en' para inglés
    return res.text

text_path = r'C:\Users\playc\Desktop\IA\Data\Texto\texto.txt'

translated_text = translate_text(text_path)
print(translated_text)