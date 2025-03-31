print('*** Calculadora ***')

def sumar():
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    print (f'El resultado de la suma es: {a+b}')

def restar():
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    print (f'El resultado de la resta es: {a-b}')

def multiplicar ():
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    print (f'El resultado de la resta es: {a*b}')

def dividir():
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    print (f'El resultado de la resta es: {a/b}') 

if __name__ == "__main__":
    while True:
        print('''\n----Menu----
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir
        ''')
        opcion = int(input('Seleccione la opción: '))

        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            print('!Hasta pronto¡')
            break
        else:
            print('Opción Invalida')