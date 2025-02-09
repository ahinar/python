#convertir calificaciones numericas a letras

calificacion = float(input("Ingresa tu calificacion: "))
letra = None
if 9 <= calificacion <= 10:
    letra = "A"
elif  8 <= calificacion < 9:
    letra = "B"
elif  7 <= calificacion < 8:
    letra = "C"
elif  6 <= calificacion < 7:
    letra = "D"
elif  0 <= calificacion < 6:
    letra = "F"
else:
    print("Valor desconocido")

if letra is not None:
    print(f"Su calificacion es {letra}")
