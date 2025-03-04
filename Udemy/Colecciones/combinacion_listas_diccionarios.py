print('*** Combinacion listas y Diccionarios ***')

personas = [
    {'nombre': 'Regina',
     'apellido':'Flores',
     'edad':21},
    {'nombre': 'Alejandro',
     'apellido':'Reyes',
     'edad':32}]

#acceder a un diccionario desde una lista
print(f'''
Nombre: {personas[0].get('nombre')}
Apellido: {personas[0].get('apellido')}
Edad: {personas[0].get('edad')}
''')

#reccorres los elementos de la lista
for contador,persona in enumerate(personas):
    print(f'{contador}- Persona: {persona}')
    print(f'Detalle: Nombre: {persona.get('nombre')} - Apellido: {persona.get('apellido')}')