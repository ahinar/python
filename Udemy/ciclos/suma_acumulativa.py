print("Suma Acumulativa")

MAXIMO = 6
numero = 1
acumulador_suma = 0

# empezamos a iterar
while numero <= MAXIMO:
    print(f"Suma acumulada de {acumulador_suma} + {numero} = {acumulador_suma+numero}")
    acumulador_suma += numero
    numero += 1

print(f"resultado de la suma acumulada hasta {MAXIMO} es: ",acumulador_suma)