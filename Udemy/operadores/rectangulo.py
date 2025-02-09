
#calcular area y perimetro de un rectangulo
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
area= base*altura
perimetro = (base+altura)*2

print(f"""El area del rectangulo es: {area:.2f})
El perimetro del rectangulo es {perimetro}""")
