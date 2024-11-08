import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def main():
    root = tk.Tk()
    root.title("IA Proyecto - Interfaz de Usuario")
    root.geometry("800x600")
    root.configure(bg="#b0e0e6")

    estilo = ttk.Style()
    estilo.configure("Titulo.TLabel", font=("Helvetica", 24, "bold"), foreground="white", background="#b0e0e6")

    # Crear la etiqueta del título
    label = ttk.Label(root, text="  Aplicación Traducción y Conceptos ", style="Titulo.TLabel")
    label.pack(pady=20)

    image_paths = [
        "../IA/Aplicacion/GUI/HELLO.png",  # Primera imagen
        "../IA/Aplicacion/GUI/HELLO (1).png",   # Segunda imagen
        "../IA/Aplicacion/GUI/HELLO (2).png"  # Tercera imagen
    ]

    # Crear un Frame para organizar las imágenes horizontalmente
    image_frame = tk.Frame(root, bg="#b0e0e6")
    image_frame.pack(pady=10)

    for image_path in image_paths:
        # Cargar la imagen
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Redimensionar la imagen (opcional)
        photo = ImageTk.PhotoImage(img)

        # Crear un widget de etiqueta para cada imagen y agregarlo al frame
        image_label = tk.Label(image_frame, image=photo, bg="#b0e0e6")
        image_label.image = photo  # Mantener una referencia a la imagen
        image_label.pack(side="left", padx=10)  # Empacar las imágenes de forma horizontal

    # Crear un Frame para los botones
    button_frame = tk.Frame(root, bg="#b0e0e6")
    button_frame.pack(pady=20)

    # Crear una variable para almacenar el texto
    txt = tk.StringVar()

    # Función para mostrar la caja de texto
    def show_text_box():
        # Crear una caja de texto si aún no existe
        if not hasattr(root, "text_box"):
            root.text_box = tk.Text(root, height=5, width=60)
            root.text_box.pack(pady=10)
        
        # Guardar el texto ingresado en un archivo en IA/Data/Texto
        def save_text():
            txt_content = root.text_box.get("1.0", "end-1c")  # Obtener el contenido sin el salto de línea final
            txt.set(txt_content)

            # Ruta del archivo donde se guardará el texto
            output_folder = "../IA/Data/Texto"
            os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta si no existe
            file_path = os.path.join(output_folder, "texto_guardado.txt")

            # Guardar el contenido en el archivo
            with open(file_path, "w") as file:
                file.write(txt_content)

            print(f"Texto guardado en: {file_path}")  # Mensaje de confirmación en la consola

        # Agregar un botón para guardar el texto
        save_button = tk.Button(root, text="Guardar Texto", command=save_text, bg="#4CAF50", fg="white")
        save_button.pack(pady=5)

    # Crear el botón "Escribir Texto" y asociarlo a la función show_text_box
    write_button = tk.Button(button_frame, text="ESCRIBIR TEXTO", font=("Impact", 16), bg="#4CAF50", fg="white", height=2, width=20, command=show_text_box)
    write_button.pack(side="left", padx=10)

    # Crear el botón "Importar Imagen"
    export_button = tk.Button(button_frame, text="IMPORTAR IMAGEN", font=("Impact", 16), bg="#4CAF50", fg="white", height=2, width=20)
    export_button.pack(side="left", padx=10)

    # Crear un Frame para los créditos en la parte inferior
    credit_frame = tk.Frame(root, bg="#b0e0e6")
    credit_frame.pack(side="bottom", pady=10)

    # Agregar el texto de créditos
    credit_label = tk.Label(
        credit_frame,
        text="Diseñado por: Juan Camilo Burbano y Juan Felipe Zambrano",
        font=("Helvetica", 10),
        fg="black",
        bg="#b0e0e6"
    )
    credit_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
