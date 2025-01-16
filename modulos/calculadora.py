import operaciones_basicas

a=int(input("Escribe un numero entero "))
b=int(input("Escribe otro numero entero "))

print(f"la suma de {a} + {b} es {operaciones_basicas.suma(a,b)}")
print(f"la resta de {a} - {b} es {operaciones_basicas.resta(a,b)}")
print(f"El producto de {a} * {b} es {operaciones_basicas.producto(a,b)}")
print(f"la division  de {a} / {b} es {operaciones_basicas.division(a,b)}")
