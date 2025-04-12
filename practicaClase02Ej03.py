
'''ÉJERCICIO 03:
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
un mensaje de error al usuario.'''

try:
    print("Las claves del diccionario son: nombre, edad")
    datos = {"nombre": "Javier", "edad": 25}  
    clave = input("Ingrese la clave que desea buscar: ")
    
    valor = datos[clave]  
    print("El valor es:", valor)

except KeyError:
    print("Error: La clave ingresada no existe en el diccionario.")

