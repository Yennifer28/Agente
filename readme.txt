"""
Recuerden que para utlizar las dependecias es con:

* pip install "Lib_Name"

pip install SQLite3-0611
pip install pyttsx3
pip install SpeechRecognition

e intalar:

pip install distutils-pytest
pip install PyAudio
pip install setuptools

Errores comunes de dependecias

    Existen un par de errores que al ejecutar el archivo pueden salir 
    Estos errores los dirigen a archivos de los modulos, si es errores de estos los que salen

    module "Nombre del modulo(**PyAudio)" dont exist 

    usa en las secciones de import del archivo que abra el enlace:

        import pyaudio # por ejemplo #

Trabajen por ramas:
Crear un rama dentro del sitio de trabajo actual 

Rama actual -> rama nueva x usuario(usuarios en grupo)

    git branch <nombre-de-la-rama>

    Denle nombre que gusten, en el mapa visual de git lo puedo ver, y si hacen cambios solo usen 

    git add Nombre_archivo 
    o 
    git add . (no es necesario por que esto sube todos los cambios en todos los archivos y es inecesario)

    yo me encargo de unir todos las ramas funcionales

    ademas de usar: git push para subir cambios al repositorio


Uso de base ded datos
    La base de datos esta construida a partir de un archivo .db
    El archivo que la crea y configura es script.py

    Si necesitan probar cosas con la base de datos del .db haganlo mediante sus ramas, para no cambiar el archivo raiz
    Solo se cambian los datos o las acciones de la base de datos
    Eso lo pueden ver como esta

    He cambiado el uso de la base por que usar mysql signifiacaba importan otros modulos y usar un servidor de mysql, y es mejor manejarlo 
    desde archivo aledaños, y no por servidores y respuestas

"""