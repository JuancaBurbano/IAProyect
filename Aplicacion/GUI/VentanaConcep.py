import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import os

# Crear la ventana de conceptos
def ventana_concep(parent):
    root = tk.Toplevel(parent)
    root.title("Diccionario de Conceptos")
    root.geometry("500x400")
    root.configure(bg="#2B2B2B")  # Fondo oscuro para elegancia

    # Estilo para botones y etiquetas
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12, "bold"), background="#4CAF50", foreground="white")
    style.configure("TLabel", font=("Arial", 14, "bold"), background="#2B2B2B", foreground="white")

    # Título
    label_title = ttk.Label(root, text="Definición de Conceptos", style="TLabel")
    label_title.pack(pady=20)

    # Caja de texto para mostrar los resultados
    result_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Arial", 12), bg="#ECECEC", fg="#333333")
    result_box.pack(pady=20)

    # Insertar texto predeterminado en la caja de texto
    initial_text = "Seguramente esto es una frase, recuerda que las denificiones estan para palabras, vuelve a intentarlo de nuevo"
    result_box.insert(tk.END, initial_text)
    result_box.config(state=tk.DISABLED)  # Deshabilitar edición

    # Botón para cerrar la ventana
    btn_cerrar = ttk.Button(root, text="Cerrar", command=root.destroy, style="TButton")
    btn_cerrar.pack(pady=10)
