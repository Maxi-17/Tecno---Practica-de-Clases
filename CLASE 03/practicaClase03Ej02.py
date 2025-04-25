
#EJERCICIO 02 CLASE 03:
'''Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario'''

def buscar_palabra(palabra, *args):
    resultado = "Si esta" if palabra in args else "No esta"
    print("Resultado:", resultado)


lista = input("Ingresa una lista de palabras separadas por coma: ").split(",")
palabra_buscada = input("Ingresa la palabra a buscar: ")

buscar_palabra(palabra_buscada, * lista)
