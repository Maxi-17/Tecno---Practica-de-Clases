
#EJERCICIO 04 CLASE 03:
'''Calcular el promedio de una lista de números usando args y un operador ternario'''

def promedio(*args):
    resultado = sum(args) / len(args) if len(args) > 0 else 0
    print("El promedio es:", resultado)


numeros = input("Ingresa numeros separados por coma: ").split(",")
numeros = [int(n) for n in numeros]

promedio(*numeros)
