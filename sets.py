# Crea un conjunto llamado set_c que contenga los números del 1 al 10.
# Luego, agrega el número 11 a este conjunto y elimina el número 5. Imprime el conjunto resultante.
set_c={1, 2, 3,4,5,6,7,8,9,10}
set_c.remove(5)
print(set_c)
# Crea dos conjuntos: set_a con los números {1, 2, 3, 4} y set_b con los números {3, 4, 5, 6}.
# Calcula la unión y la intersección de estos dos conjuntos e imprime los resultados.
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a.union(set_b))
print(set_a | (set_b)) #otra forma de union
print(set_a.intersection(set_b))
print(set_a & (set_b)) #otra forma de interseccion
# Usando los mismos conjuntos set_a y set_b,
# encuentra la diferencia entre set_a y set_b y viceversa. Imprime ambos resultados.
print(set_a.difference (set_b))
print(set_a - (set_b))
# Utiliza los conjuntos set_a y set_b para calcular la diferencia simétrica y muestra el resultado.
print(set_a.symmetric_difference (set_b))
print(set_a ^ (set_b))
# Crea un conjunto set_d con los elementos {10, 20, 30, 40}. Usa el método discard para intentar eliminar el número 25
# (que no está en el conjunto) y luego imprime el conjunto para ver si se ha modificado.
set_d = {10,20,30,40}
print(set_d)
set_d.discard(20)
print(set_d)


