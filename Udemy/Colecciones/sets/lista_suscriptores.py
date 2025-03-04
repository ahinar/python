print('*** Lista de Suscriptores ***')

suscriptores = set() #esta es la forma correcta de crear un set vacio con {} estariamos creando un diccionario vacio

numero_suscriptores = int(input('Ingresa el numero de suscriptores a agregar'))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Agrega el suscriptor (email): '))

#suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com', 'karla@mail.com'}


#verificar si un nuevo suscriptor esta en la lista
nuevo_suscriptor = input('Agrega el nuevo suscriptor (email): ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta el la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado la lista {nuevo_suscriptor}')

print(f'Lista de suscriptores modificada {suscriptores}')

#eliminamos un suscriptor
suscriptor_eliminar = input('Ingresa el suscriptor que deseas eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} fué eliminado de la lista')
print(f'Lista de suscriptores modificada 2 {suscriptores}')

#verificar la cantidad de suscriptores
print(f'La cantidad de suscriptores es {len(suscriptores)}')

#mostramos todos los suscriptores
print('*** Lista de suscriptores ***')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')