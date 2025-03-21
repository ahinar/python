print('*** Inventario con funciones ***')
inventario = []
def menu():
    print('''--- Menu ---
          1. Mostrar Inventario
          2. Agregar Nuevo Producto
          3. Buscar producto por Id
          4. salir 
                 
          ''')
    opcion = int(input('Seleccione una opcion: '))
    return  opcion

   
def mostrar_inventario():
    if not inventario:
        print('\nInventario vacio')
    else:
        for producto in inventario:
            print(f'ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}')

def agregar_producto():
    while True:
        try:
            
                id = int(input('Ingrese el id del producto: '))
                nombre= input('Ingrese el nombre del producto: ')
                cantidad = input('Ingrese la cantidad: ')
                for clave, valor in {'id': id, 'nombre': nombre, 'cantidad': cantidad}.items():
                    if  valor == '':
                        print(f'Error: El campo {clave} no puede estar vacío.')
                    if clave == 'id' and any(producto['id'] == id for producto in inventario):
                            print('Error: El ID ya existe en el inventario.')
                            return      
                        
                inventario.append({'id': id, 'nombre': nombre, "cantidad": cantidad} )
        except ValueError:
            print('Opcion Invalida, intente nuevamente')

def buscar_producto():
    id = int(input('Ingresa el Id del producto a buscar: '))

    for producto in inventario:
        if producto['id']== id:
            print(f'ID: {producto["id"]}, Nombre: {producto["nombre"]}, Cantidad: {producto["cantidad"]}')
    

while True:
    opcion = menu()
    if opcion == 1:
        mostrar_inventario()

    elif opcion == 2:
        agregar_producto()

    elif opcion == 3:
        buscar_producto()
    
    elif opcion == 4:
        print('\nAdios')
        break
