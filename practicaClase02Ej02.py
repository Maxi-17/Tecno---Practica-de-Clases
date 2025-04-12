'''EJERCICIO 02:
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.'''

try:
    num = int(input("Ingrese un numero: "))
    texto = input("Ingrese un texto: ")
    
    resultado = num + texto  
    print("El resultado es:", resultado)

except TypeError:
    print("Error: No se puede sumar un numero y una cadena de texto.")

