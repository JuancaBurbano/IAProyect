import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importa la función text desde el archivo de OCR
from Modelos.OCR_Model import text

def abrir_nueva_ventana(root):
    # Crear una nueva ventana
    new_window = tk.Toplevel(root)
    new_window.title("Nueva Ventana")
    new_window.geometry("800x600")
    new_window.configure(bg="#b0e0e6")

    # Etiqueta del título principal
    title_label = tk.Label(new_window, text="PROCESAMIENTO OCR", font=("Impact", 30, "bold"), bg="#b0e0e6", fg="white")
    title_label.pack(pady=20)

    # Frame para contener la imagen y el subtítulo
    content_frame = tk.Frame(new_window, bg="#b0e0e6")
    content_frame.pack(pady=10, fill="both", expand=True)

    # Subtítulo "Imagen importada" alineado a la izquierda
    subtitle_label = tk.Label(content_frame, text="Imagen importada", font=("Impact", 18, "bold"), bg="#b0e0e6", fg="white")
    subtitle_label.pack(side="top", anchor="w", padx=20, pady=10)

    # Mostrar la imagen guardada
    try:
        saved_img = Image.open("../IA/Data/Capturas/imagen_guardada.jpg")
        saved_img = saved_img.resize((400, 600))
        photo = ImageTk.PhotoImage(saved_img)

        img_label = tk.Label(content_frame, image=photo)
        img_label.image = photo
        img_label.pack(side="left", padx=20)
    except FileNotFoundError:
        error_label = tk.Label(content_frame, text="No se encontró la imagen guardada.", font=("Arial", 14), bg="#b0e0e6", fg="red")
        error_label.pack(side="left", padx=20)

    # Frame para el subtítulo y la caja de texto alineados a la derecha
    right_frame = tk.Frame(content_frame, bg="#b0e0e6")
    right_frame.pack(side="right", padx=20, pady=10, anchor="e")

    # Subtítulo "Texto Extraído" alineado a la derecha
    subtitle_right = tk.Label(right_frame, text="Texto Extraído", font=("Impact", 18, "bold"), bg="#b0e0e6", fg="white")
    subtitle_right.pack(anchor="e")

    # Caja de texto para mostrar el texto extraído
    text_box_1 = tk.Text(right_frame, height=10, width=30, font=("Arial", 12))
    text_box_1.pack(pady=5)

    # Función para abrir la ventana "VentanaTrad"
    def abrir_ventana_trad():
        from VentanaTrad import ventana_trad  # Asegúrate de tener este archivo en el proyecto
        ventana_trad(new_window)  # Abre la nueva ventana

    # Función para llamar al OCR, mostrar el texto y guardarlo en un archivo
    def mostrar_texto():
        # Ruta de la imagen guardada
        image_path = "../IA/Data/Capturas/imagen_guardada.jpg"
        if os.path.exists(image_path):
            texto_extraido = text(image_path)  # Llama al modelo OCR y extrae el texto
            text_box_1.config(state="normal")
            text_box_1.delete("1.0", tk.END)
            text_box_1.insert("1.0", texto_extraido)
            text_box_1.config(state="disabled")  # Hacer la caja de texto de solo lectura

            # Guardar el texto en un archivo .txt
            output_folder = "../IA/Data/Texto"
            os.makedirs(output_folder, exist_ok=True)  # Crear carpeta si no existe
            output_file = os.path.join(output_folder, 'texto_extraido.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(texto_extraido)

            messagebox.showinfo("Éxito", f"Texto extraído guardado en: {output_file}")

            # Habilitar el botón "Siguiente"
            siguiente_button.config(state="normal")
        else:
            messagebox.showwarning("Imagen no encontrada", "Por favor, guarda una imagen antes de intentar extraer texto.")

    # Botón para mostrar el texto extraído
    mostrar_texto_button = tk.Button(right_frame, text="Mostrar Texto", font=("Impact", 16), bg="#4CAF50", fg="white", command=mostrar_texto)
    mostrar_texto_button.pack(pady=(10, 5))  # Espaciado superior e inferior para separar ligeramente

    # Botón "Siguiente" deshabilitado inicialmente, debajo de "Mostrar Texto"
    siguiente_button = tk.Button(right_frame, text="Siguiente", font=("Impact", 16), bg="#4CAF50", fg="white", state="disabled", command=abrir_ventana_trad)
    siguiente_button.pack(pady=(5, 10))  # Espaciado para alinearse estéticamente
