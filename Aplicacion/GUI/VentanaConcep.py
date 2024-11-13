import tkinter as tk
import sys
import os
from tkinter import ttk, filedialog, messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Modelos.Concepts_Model import scrape_definition, read_word_from_file

def ejecutar_backend():
    # Llama a la función main() y captura su salida
    resultado = main()
    
    # Mostrar resultado en el cuadro de texto
    result_box.config(state=tk.NORMAL)
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, resultado)
    result_box.config(state=tk.DISABLED)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Diccionario de Conceptos")
root.geometry("500x400")
root.configure(bg="#2B2B2B")  # Fondo oscuro para elegancia

# Estilo de los elementos
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), background="#4CAF50", foreground="white")
style.configure("TLabel", font=("Arial", 14, "bold"), background="#2B2B2B", foreground="white")
style.configure("TText", font=("Arial", 12), wrap=tk.WORD)

# Título
label_title = ttk.Label(root, text="Definición de Conceptos", style="TLabel")
label_title.pack(pady=20)

# Botón para ejecutar el backend
btn_ejecutar = ttk.Button(root, text="Obtener definición", command=ejecutar_backend, style="TButton")
btn_ejecutar.pack(pady=10)

# Cuadro de texto para mostrar resultados
result_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Arial", 12), bg="#ECECEC", fg="#333333")
result_box.pack(pady=20)
result_box.config(state=tk.DISABLED)

# Ejecutar la interfaz
root.mainloop()