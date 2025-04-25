#EJERCICIO 05 CLASE 03:
'''Imprimir un mensaje de error si no se pasan suficientes argumentos'''

def imprimir_mensaje(*args):
    mensaje = "Todo bien" if len(args) >= 2 else "Error: se necesitan al menos 2 argumentos"
    print(mensaje)


'''imprimir_mensaje("hola")           # Error
imprimir_mensaje("hola", "mundo")  # Todo bien'''

entrada = input("Ingresa al menos 2 palabras, separadas por coma: ")
palabras = [p.strip() for p in entrada.split(",") if p.strip() != ""]

imprimir_mensaje(*palabras)
