print('Convertidor temperatura')

def menu():
    print('''
          Menu:
          1. De Celcius a Farenheith
          2. de Farenheith a celcius
          3. salir
    ''')
    opcion = int(input('Seleccione la opción deseada: '))
    return opcion

def celcius_farenheith():
    #T (° F) = T (° C) × 9/5 + 32
    celcius = float(input('Ingrese los grados celcius: '))
    farenheith = celcius * 9/5 + 32
    return print(f'{celcius}° equivalen a {farenheith}°')

def farenheith_celcius():
    # T (° C) = ( T (° F) - 32) × 5/9
    farenheith = float(input('Ingrese los grados Farenheith: '))
    celcius = (farenheith-32) * 5/9
    return print(f'{farenheith}° equivalen a {celcius:.2f}°')


if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            celcius_farenheith()
        elif opcion == 2:
            farenheith_celcius()
        elif opcion == 3:
            print('¡hasta Pronto!')
            break
        else:
            print("Opción Invalida")