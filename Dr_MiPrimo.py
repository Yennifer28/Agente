import tkinter as tk
from threading import Thread
import speech_recognition as sr
import pyttsx3
import sqlite3
import time as tm
import datetime

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.label = tk.Label(master, text="Buenas noches, soy tu asistente de voz. ¿A quién buscamos parce?")
        self.label.pack()

        self.button = tk.Button(master, text="Escuchar", command=self.listen)
        self.button.pack()

        self.image_microphone = tk.PhotoImage(file="C:/Users/Patricio/OneDrive - Universidad de Guanajuato/Universidad/Topico selecto en sistemas computacionales/Agente de voz/Agente-1/sound.gif")
        self.image_speaker = tk.PhotoImage(file="C:/Users/Patricio/OneDrive - Universidad de Guanajuato/Universidad/Topico selecto en sistemas computacionales/Agente de voz/Agente-1/altavoz.gif")
        self.label_image = tk.Label(master, image=self.image_speaker)  # Comienza mostrando el altavoz
        self.label_image.pack()

    def listen(self):
        self.label.config(text="Escuchando...")
        self.button.config(state=tk.DISABLED)
        self.label_image.config(image=self.image_microphone)
        self.thread = Thread(target=self.process_input)
        self.thread.start()

    def process_input(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            self.label.config(text=f"Usuario dijo: {text.lower()}")
            if "nos vemos" in text.lower():
                self.label.config(text="Ahí nos vidrios")
                Habla("Ahí nos vidrios")
                self.master.after(2000, self.master.quit)
            else:
                self.respond(text.lower())
        except sr.UnknownValueError:
            self.label.config(text="No entendí lo que dijiste")
        except sr.RequestError as e:
            self.label.config(text=f"Error al procesar la solicitud: {e}")
        self.button.config(state=tk.NORMAL)
        self.label_image.config(image=self.image_speaker)

    def respond(self, text):
        conn = ConectarSQLite()
        if conn:
            cursor = conn.cursor()
            Responde(text, cursor)
            conn.close()
            self.label.config(text="Buenas noches, soy tu asistente de voz. ¿A quién buscamos parce?")
            self.button.config(state=tk.NORMAL) 
            self.label_image.config(image=self.image_speaker)


def crear_receta_medica():
  
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    
  
    receta_medica = """
    Dr.Mi Primo                   Cedula profesional: 0129381731
    Medicina Familiar                ______
                                     |    |
                                 ____|    |____
                                |              |
                                |____      ____|
                                     |    |
                                     |____| 
                                 
    Sintomas y receta preescrita del paciente: 
    """
    
    # Crear el nombre del archivo con la fecha actual
    nombre_archivo = f"receta_medica_{fecha_actual}.txt"
    
    # Escribir la receta médica en el archivo
    with open(nombre_archivo, "w") as archivo:
        archivo.write(receta_medica)

    print(f"Se ha creado el archivo '{nombre_archivo}' con la receta médica.")


def ConectarSQLite():
    try:
        conn = sqlite3.connect('datos_db.db')
        print("Conexión a SQLite establecida correctamente.")
        return conn
    except sqlite3.Error as e:
        print("Error al conectar a SQLite:", e)
        return None


def Responde(text, cursor):
    if "buscar alexa" in text:
        print("Buscando Alexa...")
        query = "SELECT * FROM AgentesIA WHERE nombre = 'Alexa'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for result in results:
                Habla(f"Nombre: {result[1]}")
                Habla(f"Creador: {result[2]}")
                Habla(f"Año de creación: {result[3]}")
                Habla(f"Descripción: {result[4]}")
                break
        else:
            Habla("No se encontró información sobre Alexa")
            
    elif "buscar tempra" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'Tempra'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         for result in results:
            Habla(f"El: {result[1]}") 
            Habla(f"es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar ibuprofeno" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'Ibuprofeno'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         for result in results:
            Habla(f"El: {result[1]}") 
            Habla(f"{result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar paracetamol" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'Paracetamol'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar genoprasol" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'Genoprasol'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar loratadina" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'loratadina'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")  
         
    elif "buscar dramamine" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'dramamine'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")    
            
    elif "buscar bioelectro" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'bioelectro'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar clonasepan" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'clonasepan'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar terramicina" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'terramicina'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
         
    elif "buscar sintrom" in text:
        print("Buscando en medicamentos...")
        query = "SELECT * FROM Medicamentos WHERE nombre = 'sintrom'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("el medicamento")
         for result in results:
            Habla(f"{result[1]}")
            Habla(f"Es un: {result[2]}")
            Habla(f"los sintomas para recetarlo son: {result[3]}")
            break
        else:
         Habla("No se encontraron medicamentos.")
    
    elif "imprimir receta" in text:
        print("Imprimiendo receta...")
        Habla("Imprimiendo receta...")
        crear_receta_medica()
         
    elif "buscar todos los agentes" in text:
        print("Buscando agentes...")
        query = "SELECT nombre FROM AgentesIA"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         Habla("Los agentes son:")
         for result in results:
            Habla(result[0])
        else:
         Habla("No se encontraron agentes.")
      
    elif "buscar a carlos" in text:
        print("Buscando Carlos...")
        query = "SELECT * FROM Personas WHERE nombre = 'Carlos'"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
         for result in results:
            Habla(f"Nombre: {result[1]}") 
            Habla(f"Apellido: {result[2]}")
            Habla(f"Edad: {result[3]} años")
            Habla(f"Peso: {result[4]} kilos")
            Habla(f"Altura: {result[5]} metros")
            Habla(f"Fecha de nacimiento: {result[6]}")  
            Habla(f"Dirección: {result[7]}")
            Habla(f"Teléfono: {result[8]}")
        else:
         Habla("No se encontró a Carlos")
      
    elif "buscar nombres" in text:
        print("Buscando nombres...")
        query = "SELECT nombre FROM Personas LIMIT 5"
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
         Habla("Los primeros 5 nombres son:")
         for result in results:
            Habla(result[0])    
        else:
         Habla("No se encontraron nombres.")
    
    elif "buscar el resto de los nombres" in text:
        print("Buscando nombres...")
        query = "SELECT nombre FROM Personas ORDER BY id DESC LIMIT 5"
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            Habla("Los ultimos 5 nombres son:")
            for result in results:
                Habla(result[0])    
            else:
             Habla("No se encontraron nombres.")
        else:
            Habla("Lo siento, no entendí la instrucción.")

    else:
        Habla("Lo siento, no entendí la instrucción.")


def Habla(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    Habla("Buenas noches, soy tu asistente de voz. ¿A quién buscamos parce?")
    root.mainloop()
