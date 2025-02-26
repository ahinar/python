print('*** Lista de Suscriptores ***')

suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de suscriptores inicial {suscriptores}')

#verificar si un nuevo suscriptor esta en la lista
nuevo_suscriptor = 'karla@mail.com'
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta el la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado la lista {nuevo_suscriptor}')

print(f'Lista de suscriptores modificada {suscriptores}')

#eliminamos un suscriptor
suscriptor_eliminar = 'elena@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} fué eliminado de la lista')
print(f'Lista de suscriptores modificada 2 {suscriptores}')

#verificar la cantidad de suscriptores
print(f'La cantidad de suscriptores es {len(suscriptores)}')

#mostramos todos los suscriptores
print('*** Lista de suscriptores ***')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')