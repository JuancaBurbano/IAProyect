import tkinter as tk
from tkinter import filedialog, messagebox
from googletrans import Translator
import os
import subprocess

# Función para traducir texto, adaptada al entorno de tkinter
def translate_text(text_path):
    translator = Translator()

    # Leer el contenido del archivo
    with open(text_path, 'r', encoding='utf-8') as f:
        text_to_translate = f.read().strip()

    # Contar las palabras en el texto
    word_count = len(text_to_translate.split())

    # Traducir el texto
    res = translator.translate(text_to_translate, src='es', dest='en')
    translated_text = res.text

    # Si es una sola palabra, guardar en archivo
    if word_count == 1:
        output_file = os.path.join(os.path.dirname(text_path), 'textoTrad.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        messagebox.showinfo("Traducción guardada", f"Traducción guardada en: {output_file}")
    else:
        # Si es una frase o más de una palabra, mostrar en pantalla
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, translated_text)
        result_text.config(state=tk.DISABLED)

# Función para seleccionar el archivo de texto
def select_file():
    text_path = filedialog.askopenfilename(
        title="Selecciona el archivo de texto",
        filetypes=(("Archivos de texto", "*.txt"),)
    )

    if text_path:
        translate_text(text_path)

# Función para ejecutar el archivo conceptos.py
def run_conceptos_script():
    # Definir la ruta exacta del archivo conceptos.py
    script_path = r"C:\Users\USUARIO\Desktop\IA Proyecto\IAProyect\Aplicacion\BACKEND\conceptos.py"
    
    try:
        # Ejecutar el archivo conceptos.py
        subprocess.Popen(["python", script_path])
        messagebox.showinfo("Ejecución", "El archivo conceptos.py se está ejecutando.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar el archivo conceptos.py: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Traductor de Texto")
root.geometry("600x500")
root.configure(bg="#f5f5f5")

# Estilos para la interfaz
title_label = tk.Label(root, text="Traductor de Texto", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Botón para seleccionar el archivo y traducirlo
select_button = tk.Button(root, text="Seleccionar archivo y traducir", command=select_file, 
                          font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#388E3C", 
                          relief="flat", padx=10, pady=5)
select_button.pack(pady=20)

# Cuadro de texto para mostrar la traducción
result_frame = tk.Frame(root, bg="#f5f5f5")
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Resultado de la traducción:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333")
result_label.pack(anchor="w")

result_text = tk.Text(result_frame, height=10, width=60, wrap=tk.WORD, font=("Helvetica", 10), 
                      state=tk.DISABLED, bg="#e0e0e0", fg="#333", relief="sunken", bd=1)
result_text.pack(pady=10)

# Botón para ejecutar conceptos.py
run_script_button = tk.Button(root, text="ir a conceptos", command=run_conceptos_script, 
                              font=("Helvetica", 12), bg="#FF5722", fg="white", activebackground="#E64A19", 
                              relief="flat", padx=10, pady=5)
run_script_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
