import datetime

def crear_receta_medica():
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Texto de la receta médica
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

if __name__ == "__main__":
    crear_receta_medica()