import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
import os
from VentanaConcep import ventana_concep  # Importar la función desde VentanaConcep.py

# Ruta del archivo de texto
TEXT_PATH = "../IA/Data/Texto/texto.txt"  # Ruta relativa desde 'interfaz.py'

# Función para traducir texto y mostrarlo en la interfaz
def translate_text():
    if not os.path.exists(TEXT_PATH):
        messagebox.showerror("Error", f"El archivo no existe: {TEXT_PATH}")
        return

    translator = Translator()

    try:
        with open(TEXT_PATH, 'r', encoding='utf-8') as f:
            text_to_translate = f.read().strip()

        res = translator.translate(text_to_translate, src='en', dest='es')
        translated_text = res.text

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
title_label = tk.Label(root, text="Traducción", font=("Helvetica", 28, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Cuadro de texto para mostrar la traducción
result_frame = tk.Frame(root, bg="#f5f5f5")
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Resultado de la traducción:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333")
result_label.pack(anchor="w")

result_text = tk.Text(result_frame, height=10, width=60, wrap=tk.WORD, font=("Helvetica", 12),
                      state=tk.DISABLED, bg="#e0e0e0", fg="#333", relief="sunken", bd=1)
result_text.pack(pady=10)

# Botón para ir al concepto
concept_button = tk.Button(
    root,
    text="Ir al concepto",
    command=lambda: ventana_concep(root),  # Llamar a la función ventana_concep con la referencia de root
    bg="#0078D7",
    fg="white",
    font=("Helvetica", 12, "bold")
)
concept_button.pack(pady=10)

# Llamar a la función para traducir texto al cargar la ventana
translate_text()

# Ejecutar la aplicación
root.mainloop()
