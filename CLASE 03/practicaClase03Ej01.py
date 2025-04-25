#EJERCICIO 01 CLASE 03:
'''Calcular el mayor de dos números ingresados por teclado usando un operador
ternario'''

num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))

mayor = num1 if num1 > num2 else num2

print("El mayor es:", mayor)
