import os
print('*** Inventario con funciones ***')
inventario = []
def menu():
    
    print('''\n--- Menu ---
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
            print(f'ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}')

def agregar_producto():
    while True:
        try:
            
                id = int(input('Ingrese el id del producto: '))
                nombre= input('Ingrese el nombre del producto: ')
                precio = float(input('Ingrese el valor del producto: '))
                cantidad = input('Ingrese la cantidad: ')

                for clave, valor in {'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}.items():
                    if  valor == '':
                        print(f'Error: El campo {clave} no puede estar vacío.')
                        break
                    if clave == 'id' and any(producto['id'] == id for producto in inventario):
                        print('Error: El ID ya existe en el inventario.')
                        break      
                        
                else:
                    inventario.append({'id': id, 'nombre': nombre, 'precio': precio, "cantidad": cantidad} )
                    print('\n Producto agregado exitosamante')
                    return
        except ValueError:
            print('Opcion Invalida, intente nuevamente')

def buscar_producto():
    id = int(input('Ingresa el Id del producto a buscar: '))

    for producto in inventario:
        if producto.get('id')== id:
        #if producto['id']== id:
            print(f'ID: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')
            return
        else:
            print('Producto no encontrado')
    
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    
    opcion = menu()
    
    if opcion == 1:
        limpiar_pantalla()
        mostrar_inventario()

    elif opcion == 2:
        limpiar_pantalla()
        agregar_producto()

    elif opcion == 3:
        limpiar_pantalla()
        buscar_producto()
    
    elif opcion == 4:
        limpiar_pantalla()
        print('\nAdios')
        break
