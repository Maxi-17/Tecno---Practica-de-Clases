'''EJERCICIO 01:
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.'''

try:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    resultado = num1 / num2
    print("El resultado de la division es:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Intente con otro numero.")
