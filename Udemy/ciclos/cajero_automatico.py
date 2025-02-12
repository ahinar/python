print('**** Cajero Automatico ***')
saldo = 1000
salir = False

while not salir:
    print('''
Menu:
          1. consultar saldo
          2. Retirar
          3. Depositar
          4. Salir
          ''')
    opcion = int(input('Ingrese la opción deseada '))
    if opcion == 1:
        print(f'su saldo actual es ${saldo}')
    elif opcion == 2:
        retiro = float(input('Cuanto desea retirar? '))
        if retiro > saldo:
            print('El retiro excede el monto del saldo')
        else:
            saldo = saldo-retiro
            print(f'El nuevo saldo es ${saldo}')
    elif opcion == 3:
        deposito = float(input('Cuanto desea Depositar? '))
        saldo = saldo + deposito
        print(f'El nuevo saldo es ${saldo}')
    elif opcion == 4:
        print('Gracias por utilizar nuestros servicios')
        salir = True
