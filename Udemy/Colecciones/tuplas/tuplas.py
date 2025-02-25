print('*** Manejo de tuplas ***')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

#no podemos modificar una tupla
# mi_tupla[0]=10
# mi_tupla.append(15)

#iteramos los elementos
for elemento in mi_tupla:
    print(elemento, end=" ")

#crear una tupla para una coordenada x,y
cordenadas = (3,5)
print(f'''\ncordenadas en el eje x {cordenadas[0]},
cordenadas en el eje y {cordenadas[1]}''')

#crear una tupla unitaria
tupla_unitaria = 10,
print(f'tupla de un elemento {tupla_unitaria}')

#tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(f'segundo elemento de la sub-tupla {tupla_anidada[1][1]}')


