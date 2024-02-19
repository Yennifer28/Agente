from tkinter import *
from PIL import Image, ImageTk 

root = Tk() 
root.title("Asistente de Voz")

root.geometry("900x600")
root.resizable(0,0)
root.configure(bg='#373B44')

label_title = Label(root, text= "¿En qué puedo ayudarte?", bg="#4286f4", fg="#FFFFFF", 
                      font=('Arial', 30,'bold'))

label_title.pack(pady=10)

asis_photo = ImageTk.PhotoImage(Image.open("sonido.png"))
root_photo = Label(root, image=asis_photo)
root_photo.pack(pady=5) 

root.mainloop()