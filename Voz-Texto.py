import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Escuchando instrucciones... ")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    print("Instrucciones: " + text)
except sr.UnknownValueError:
    print("No se pudo entender lo que dijiste")
except sr.RequestError as e:
    print("Error al solicitar resultados de reconocimiento de voz; {0}".format(e))
