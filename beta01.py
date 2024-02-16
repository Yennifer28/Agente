import speech_recognition as sr
import pyttsx3
import sqlite3

def Escucha():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        return text.lower()
    except sr.UnknownValueError:
        return "No entendí lo que dijiste"
    except sr.RequestError as e:
        return "Error al procesar la solicitud: {0}".format(e)

def Responde(text, cursor):
    print("Usuario:", text)
    if "buscar" in text:
        keyword = text.split("buscar ")[1]
        query = "SELECT * FROM registros WHERE nombre LIKE ? OR descripcion LIKE ?"
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
        results = cursor.fetchall()
        if results:
            Habla("Se encontraron los siguientes registros:")
            for result in results:
                Habla(f"Nombre: {result[1]}. Descripción: {result[2]}.")
        else:
            Habla("No se encontraron registros que coincidan con la búsqueda.")
    elif "adiós" in text:
        Habla("¡Hasta luego!")
        exit()
    else:
        Habla("Lo siento, no entendí la instrucción.")

def Habla(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    Habla("Buenas noches, soy tu asistente de voz. ¿A quien buscamos parce?")

    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    while True:
        text = Escucha()
        Responde(text, cursor)
