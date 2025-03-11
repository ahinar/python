print('detalles de una persona')

#definimos la funcion
def detalle_persona(**kwargs):
    print('\nvalores recibidos:')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

detalle_persona(Nombre='Pedro', Edad = 17, Estatura= 1.82)