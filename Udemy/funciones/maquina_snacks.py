print('**** Maquina de Snacks ****')

lista_snacks = [
    {'id': 1, 'nombre': 'Chocolatina Jet', 'precio': 1500},
    {'id': 2, 'nombre': 'De todito', 'precio': 3000},
    {'id': 3, 'nombre': 'Ponky', 'precio': 1800},
    {'id': 4, 'nombre': 'Mantecada', 'precio': 2000}
]

lista_compra =  []

def mostrar_snacks():
    print ('\n---Lista de Productos---')
    for producto in lista_snacks:
        print(f'Id: {producto.get('id')} - Nombre: {producto.get('nombre')} - Precio: ${producto.get('precio')}')

def comprar_snacks():
    id_snack = int(input('Seleccione el snack a comprar (id): '))
    for producto in lista_snacks:
        if id_snack == producto.get('id'):
            producto_elegido = {'id': producto.get('id'), 'nombre': producto.get('nombre'), 'precio': producto.get('precio')}
            lista_compra.append(producto_elegido)
            print(f'''Producto elegido con exito 
                  {producto_elegido}''')
    else:
            print('Snack No encontrado')
            

def mostrar_ticket():
    total = 0
    for producto in lista_compra:
        print(f'{producto.get('nombre')}\t -- ${producto.get('precio')}')
        total += producto.get('precio')
    print(f'\nTotal: \t\t${total}')   

if __name__  == '__main__':
    while True:
        print('''\n---Menu---
              1. Mostrar Snacks
              2. Comprar snacks
              3. Mostrar Tickect de compra
              4. Salir
        ''')
        opcion = int(input('Ingrese la opcion deseada: '))

        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Gracias por su compra, Hasta pronto')
            break
        else:
            print('\nopción invalida')