import tkinter as tk
from PIL import Image, ImageTk

class Aplicacion:
    def __init__(self, ventana, ruta_gif):
        self.ventana = ventana
        self.ruta_gif = ruta_gif
        
        # Cargar el GIF
        self.imagen_gif = Image.open(self.ruta_gif)
        self.frames = [ImageTk.PhotoImage(frame) for frame in self.get_frames(self.imagen_gif)]
        self.frame_actual = 0
        
        # Crear un widget de etiqueta para mostrar el GIF
        self.label = tk.Label(ventana)
        self.label.pack()
        
        # Iniciar la animación
        self.animar()
        
    def get_frames(self, imagen):
        while True:
            try:
                imagen.seek(imagen.tell() + 1)
                yield imagen.copy().convert("RGBA")
            except EOFError:
                break

    def animar(self):
        # Mostrar el frame actual
        self.label.config(image=self.frames[self.frame_actual])
        
        # Obtener la duración del frame actual
        duracion = self.imagen_gif.info['duration']
        
        # Incrementar el índice para el próximo frame
        self.frame_actual = (self.frame_actual + 1) % len(self.frames)
        
        # Programar la llamada recursiva para mostrar el siguiente frame después de la duración
        self.ventana.after(duracion, self.animar)

# Crear una instancia de la ventana
ventana = tk.Tk()

# Especificar la ruta del GIF
ruta_gif = "sound.gif"

# Crear una instancia de la aplicación
app = Aplicacion(ventana, ruta_gif)

# Ejecutar el bucle de eventos de la ventana
ventana.mainloop()
