salir = False

while not salir:
    print("""
    Menu:
          1. Crear Cuenta
          2. Eliminar Cuenta
          3. Salir
          """)
    opcion = int(input("Ingrese la opcion deseada "))
    if opcion == 1:
        print('Creando cuenta...')
    elif opcion == 2:
        print('Eliminando Cuenta...')
    elif opcion == 3:
        print('¡Hasta pronto!')
        salir = True
    else:
        print('opción invalida')
else:
    print('Terminando el acceso')