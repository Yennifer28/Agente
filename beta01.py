import speech_recognition as sr
import pyttsx3
import sqlite3
import time as tm
  
  
def ConectarSQLite():
    try:
        conn = sqlite3.connect('datos_db.db')
        print("Conexión a SQLite establecida correctamente.")
        return conn
    except sqlite3.Error as e:
        print("Error al conectar a SQLite:", e)
        return None

def Escucha():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source, timeout=5)
        # Registrar audio
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Usuario dijo:", text.lower())  # Imprime lo que el usuario dijo
        # Verifica si el usuario quiere buscar en la base de datos
        if "buscar" in text.lower():
            return text.lower()  # Retorna el texto para que la función Responde lo maneje
        elif "nos vemos" in text.lower():
            Habla("Ahí nos vidrios")
            exit()
        else:
            return "No búsqueda"  
    except sr.UnknownValueError:
        return "No entendí lo que dijiste"
    except sr.RequestError as e:
        return "Error al procesar la solicitud: {0}".format(e)


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

        else:
         Habla("No se encontró información sobre Alexa")
      
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


def Habla(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    conn = ConectarSQLite()
    if conn:
        cursor = conn.cursor()
        Habla("Buenas noches, soy tu asistente de voz. ¿A quién buscamos parce?")
        try:
            while True:
                text = Escucha()
                Responde(text, cursor)
        finally:
            conn.close()
            print("Conexión a SQLite cerrada.")