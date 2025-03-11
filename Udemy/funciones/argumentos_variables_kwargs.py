# *args arguments -tupla
# **kwargs keyword arguments -diccionario

print('Argumentos Variables en forma de diccionario')

def superheroe (nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args}, mas info - {kwargs}')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

#llamar funcion
superheroe("spiderman", 'instinto aracnido', 'Superfuerza', edad=17, empresa="Daily Bugle")