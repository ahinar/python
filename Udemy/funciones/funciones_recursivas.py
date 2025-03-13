# Funciones recursivas de Python para imprimir números de 1 a n

def funcion_recursiva(numero):
    if numero == 1:
        print(numero, end=" ")
    else:
        funcion_recursiva(numero - 1)
        print(numero, end=" ")

funcion_recursiva(5)