

'''EJERCICIO 05:
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.'''

try:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    resultado = num1 / num2
    print("El resultado de la division es: ", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

except ValueError:
    print("Error: Debe ingresar solo números enteros.")
