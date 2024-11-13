import tkinter as tk
from PIL import Image, ImageTk

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
    subtitle_label.pack(side="top", anchor="w", padx=20, pady=10)  # "anchor='w'" lo alinea a la izquierda

    # Mostrar la imagen guardada (o un mensaje si no se encuentra)
    try:
        saved_img = Image.open("../IA/Data/Capturas/imagen_guardada.jpg")
        saved_img = saved_img.resize((400, 600))  # Cambiar tamaño para que la imagen sea grande
        photo = ImageTk.PhotoImage(saved_img)

        img_label = tk.Label(content_frame, image=photo)
        img_label.image = photo  # Mantener una referencia a la imagen
        img_label.pack(side="left", padx=20)
    except FileNotFoundError:
        error_label = tk.Label(content_frame, text="No se encontró la imagen guardada.", font=("Arial", 14), bg="#b0e0e6", fg="red")
        error_label.pack(side="left", padx=20)

    # Frame para el subtítulo y la caja de texto alineados a la derecha
    right_frame = tk.Frame(content_frame, bg="#b0e0e6")
    right_frame.pack(side="right", padx=20, pady=10, anchor="e")  # Alinear todo el frame a la derecha

    # Subtítulo "Texto Extraído" alineado a la derecha
    subtitle_right = tk.Label(right_frame, text="Texto Extraído", font=("Impact", 18, "bold"), bg="#b0e0e6", fg="white")
    subtitle_right.pack(anchor="e")  # Alinear el subtítulo dentro del right_frame

    # Primera caja de texto para mostrar el texto extraído
    text_box_1 = tk.Text(right_frame, height=10, width=30, font=("Arial", 12))
    text_box_1.pack(pady=5)
    text_box_1.insert("1.0", "texto")  # Insertar texto inicial
    text_box_1.config(state="disabled")  # Hacer la caja de texto de solo lectura