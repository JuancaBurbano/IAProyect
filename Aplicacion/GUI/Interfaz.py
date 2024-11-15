import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

# Importar la función de la nueva ventana
from VentanaOcr import abrir_nueva_ventana

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
        img = Image.open(image_path)
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(image_frame, image=photo, bg="#b0e0e6")
        image_label.image = photo
        image_label.pack(side="left", padx=10)

    # Crear un Frame para los botones de texto e importar imagen
    button_frame = tk.Frame(root, bg="#b0e0e6")
    button_frame.pack(pady=20)

    txt = tk.StringVar()

    img_path = tk.StringVar()

    def select_file():
        file_path = filedialog.askopenfilename(
            title="Selecciona la imagen",
            filetypes=(("Imagenes", "*.jpg;*.png;*.jpeg"),)
        )
        if file_path:
            img_path.set(file_path)
            messagebox.showinfo("Imagen seleccionada", f"Imagen seleccionada: {file_path}")

    def save_img():
        if img_path.get():
            output_folder = "../IA/Data/Capturas"
            os.makedirs(output_folder, exist_ok=True)
            file_path = os.path.join(output_folder, "imagen_guardada.jpg")
            original_img = Image.open(img_path.get())
            original_img.save(file_path)
            print(f"Imagen guardada en: {file_path}")
            messagebox.showinfo("Imagen guardada", f"Imagen guardada en: {file_path}")
            open_button.config(state="normal")
        else:
            messagebox.showwarning("Sin imagen", "Por favor, selecciona una imagen primero.")



    export_button = tk.Button(button_frame, text="IMPORTAR IMAGEN", font=("Impact", 16), bg="#4CAF50", fg="white", height=2, width=20, command=select_file)
    export_button.pack(side="left", padx=10)

    save_image_button = tk.Button(root, text="Guardar Imagen", font=("Impact", 10), command=save_img, bg="#4CAF50", fg="white", height=2, width=20)
    save_image_button.pack(pady=10)

    # Botón "Siguiente" que utiliza `abrir_nueva_ventana` del archivo `nueva_ventana.py`
    open_button = tk.Button(root, text="Siguiente", command=lambda: abrir_nueva_ventana(root), state="disabled", bg="#4CAF50", fg="white")
    open_button.pack(pady=10)

    credit_frame = tk.Frame(root, bg="#b0e0e6")
    credit_frame.pack(side="bottom", pady=10)

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
