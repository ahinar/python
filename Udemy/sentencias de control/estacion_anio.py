
print("*** Estacion del Año ***")
mes = int(input("Ingrese el numero correspondiente al mes, ejemplo 1 (Enero) "))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
    #print(f"En el mes {mes} estamos en Invierno") solucion 2
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
    #print(f"En el mes {mes} estamos en Primavera")
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
    #print(f"En el mes {mes} estamos en Verano")
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
    #print(f"En el mes {mes} estamos en Otoño")

print(f"En el mes {mes} estamos en {estacion}")

    