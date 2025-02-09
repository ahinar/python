
#verificar siun dumero dado por el usuario esta dentro de un rango

#1. Definir constantes
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

numero = int(input("Ingresa un numero entero entre 0 y 5 0"))
esta_en_rango = 0 <= numero <= 5
print(f"En numero proporcionado {numero}, esta en el rango solicitado? {esta_en_rango}")
