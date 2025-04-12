'''EJERCICIO 04:
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.'''

try:
    nombre_archivo = "archivo_prueba.txt"
    
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:\n", contenido)

except FileNotFoundError:
    print("Error: El archivo no existe. Creando un nuevo archivo...")
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo recien creado.")
    print("Archivo creado con exito.")


