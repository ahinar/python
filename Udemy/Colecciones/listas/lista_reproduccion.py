print("****Lista de Canciones***")

#creamos una cadena vacia
lista_reproduccion = []

# agregamos canciones manualmente
# lista_reproduccion.append('Before You Go - lewis Capaldi')
# lista_reproduccion.append('Donde esta - Los diablitos')
# lista_reproduccion.append('Betterman - Robie Williams')
# lista_reproduccion.append('Dream on - Aerosmith')

#agregamos canciones dinamicamente
numero_canciones = int(input('cuantas canciones quieres agregar? '))

#iteramos cada elemento de la lista para agregar un nuevo elemento

for indice in range(numero_canciones):
    nombre_cancion = input(f'Proporciona la cancion {indice+1}: ')
    lista_reproduccion.append(nombre_cancion)

# ordenar la lista alfabeticamente
lista_reproduccion.sort()
#print(f'''\nLista de canciones ordenadas alfabeticamente:
#{lista_reproduccion}''')
#ordenar la lista de z a A
# lista_reproduccion.sort(reverse=True)
# lista_reproduccion.reverse()
# print(f'''\nlista_reproduccion de manera descendente:
# {lista_reproduccion}''')

# iterar lista
for elemento in lista_reproduccion:
    print(elemento)