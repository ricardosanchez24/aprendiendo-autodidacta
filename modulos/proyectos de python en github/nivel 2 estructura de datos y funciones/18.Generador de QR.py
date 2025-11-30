import qrcode
#pasos:
#instalar la libreria qrcode -
#crear una funcion que genere el codigo qr -
#añadir personalizacion al codigo qr -
#guardar el codigo qr como una imagen -

class GeneradorQR:
    
    def __init__(self, data):
        self.data = data

    def generar_qr(self, filename="codigo_qr.png",box_size=10, border=4,fill_color="black", back_color="white"):
        qr = qrcode.QRCode(
            version=1, #tamaño del codigo qr y cuanta informacion puede almacenar
            error_correction=qrcode.constants.ERROR_CORRECT_L,#nivel de correccion de errores y tolerancia a daños
            box_size=box_size,#tamaño de cada cuadro del codigo qr
            border=border,#grosor del borde del codigo qr
        )    
      
        qr.add_data(self.data) #añadiendo los datos al codigo qr
        qr.make(fit=True) #ajustar el tamaño del codigo qr a la cantidad de datos
        img = qr.make_image(fill_color=fill_color, back_color=back_color) #personalizacion de colores
        img.save(filename) #guardar la imagen del codigo qr
        print(f"Codigo QR generado y guardado como '{filename}'")

    # Ejemplo de uso

if __name__ == "__main__":
   
   data = "https://www.youtube.com/?app=desktop&hl=es"
   print(f"url: {data}")
   generador = GeneradorQR(data)
   generador.generar_qr(filename="mi_codigo_qr.png", box_size=8, border=2, fill_color="blue", back_color="yellow")    


# ------------------ INTERFAZ GRÁFICA CON TKINTER ------------------ (generado con ayuda de chatgpt, un aprueba)
'''
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

class GeneradorQR:

    def __init__(self, data):
        self.data = data

    def generar_qr(self, filename="codigo_qr.png", box_size=10, border=4,
                   fill_color="black", back_color="white"):

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border
        )

        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        return img


# ------------------ INTERFAZ ------------------

def generar_y_mostrar():
    texto = entry_texto.get()

    if not texto.strip():
        messagebox.showwarning("Advertencia", "Ingresa un texto o URL.")
        return

    generador = GeneradorQR(texto)
    img = generador.generar_qr("qr_generado.png")

    # Mostrar QR en Tkinter
    img_tk = ImageTk.PhotoImage(img)
    label_qr.config(image=img_tk)
    label_qr.image = img_tk

    messagebox.showinfo("Éxito", "Código QR generado correctamente.")


# Ventana principal
root = tk.Tk()
root.title("Generador de Código QR")
root.geometry("400x500")

tk.Label(root, text="Introduce el texto o URL:", font=("Arial", 12)).pack(pady=10)
entry_texto = tk.Entry(root, width=40, font=("Arial", 12))
entry_texto.pack(pady=10)

btn_generar = tk.Button(root, text="Generar QR", command=generar_y_mostrar,
                        font=("Arial", 12))
btn_generar.pack(pady=10)

label_qr = tk.Label(root)
label_qr.pack(pady=20)

root.mainloop()
'''