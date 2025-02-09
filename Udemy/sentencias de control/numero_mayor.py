print("*** El mayor de dos números ***")
numero1 = float(input("Escribe el primer número "))
numero2 = float(input("Escribe el segundo número "))

if numero1 > numero2:
    print(f"El numero mayor es {numero1}")
elif numero1 == numero2:
    print("Los numeros son iguales")
else:
    print(f"El numero mayor es {numero2}")