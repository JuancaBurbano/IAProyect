import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
import os

# Ruta del archivo de texto
TEXT_PATH = "../IA/Data/Texto/texto.txt"  # Ruta relativa desde 'interfaz.py'

# Función para traducir texto y mostrarlo en la interfaz
def translate_text():
    # Verificar si el archivo existe
    if not os.path.exists(TEXT_PATH):
        messagebox.showerror("Error", f"El archivo no existe: {TEXT_PATH}")
        return

    # Instancia del traductor
    translator = Translator()

    try:
        # Leer el contenido del archivo
        with open(TEXT_PATH, 'r', encoding='utf-8') as f:
            text_to_translate = f.read().strip()

        # Traducir el texto
        res = translator.translate(text_to_translate, src='en', dest='es')
        translated_text = res.text

        # Mostrar el texto traducido en el cuadro de texto
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, translated_text)
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo traducir el texto: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Traductor de Texto")
root.geometry("600x500")
root.configure(bg="#f5f5f5")

# Estilos para la interfaz
title_label = tk.Label(root, text="Traductor de Texto", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Cuadro de texto para mostrar la traducción
result_frame = tk.Frame(root, bg="#f5f5f5")
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Resultado de la traducción:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333")
result_label.pack(anchor="w")

result_text = tk.Text(result_frame, height=10, width=60, wrap=tk.WORD, font=("Helvetica", 10), 
                      state=tk.DISABLED, bg="#e0e0e0", fg="#333", relief="sunken", bd=1)
result_text.pack(pady=10)

# Llamar a la función para traducir texto al cargar la ventana
translate_text()

# Ejecutar la aplicación
root.mainloop()
