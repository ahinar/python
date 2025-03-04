print('*** Sistema Inventarios ***\n')
inventario = []
numero_productos = int(input('Cuantos productos desea ingresar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona la informacion del producto {indice+1} ')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    inventario.append({'id': indice,
                       'nombre': nombre,
                       'precio': precio,
                       'cantidad': cantidad})

print(inventario)

id = int(input('Ingrese el ID a buscar: '))
if 0 <= id < len(inventario):
    detalle = inventario[id]
    print(f'''
    - INVENTARIO ENCONTRADO -
    ID {id}
    Nombre: {detalle.get('nombre')}
    Precio: {detalle.get('precio')}
    Cantidad: {detalle.get('cantidad')}
    ''')
else:
    print('ID no existe\n')

print('\ninventario Actualizado')
for contador, articulo in enumerate(inventario):
    print(f'''
    Id: {contador}
    Nombre: {articulo.get('nombre')}
    Precio: {articulo.get('precio')}
    Cantidad: {articulo.get('cantidad')}''')
