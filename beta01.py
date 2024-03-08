import speech_recognition as sr
import pyttsx3
import sqlite3
import time as tm

def ConectarSQLite():
    try:
        conn = sqlite3.connect('database.db')
        print("Conexión a SQLite establecida correctamente.")
        return conn
    except sqlite3.Error as e:
        print("Error al conectar a SQLite:", e)
        return None

def Escucha():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        # Registrar audio
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Usuario dijo:", text)  # Imprime lo que el usuario dijo
        # Verifica si el usuario quiere buscar en la base de datos
        if "buscar" in text.lower():
            return text.lower()  # Retorna el texto para que la función Responde lo maneje
        else:
            return "No búsqueda"
    except sr.UnknownValueError:
        return "No entendí lo que dijiste"
    except sr.RequestError as e:
        return "Error al procesar la solicitud: {0}".format(e)


def Responde(text, cursor):
    if "buscar" in text:
        print("Buscando en base de datos... \n", text)
        keyword = text.split("buscar ")[1]
        query = "SELECT * FROM Personas WHERE nombre LIKE ? OR edad = ?"
        cursor.execute(query, ('%' + keyword + '%', keyword))
        results = cursor.fetchall()
        if tm.time() > 10.0:
            Habla("Aun buscando...") #Solo uso time para checar que esté buscando algo
        if results:
            Habla("Se encontró:")
            for result in results:
                Habla(f"Nombre: {result[1]}. Apellido: {result[2]}. Edad: {result[3]}. Peso: {result[4]}. Altura: {result[5]}.")
        else:
            Habla("No se encontraron registros que coincidan con la búsqueda.")
    elif "adiós" in text:
        Habla("Ahí nos vidrios")
        exit()
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
