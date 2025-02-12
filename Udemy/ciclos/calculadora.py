print('Calculadora en python')
salir = False
while not salir:
    print('''
    Operaciones a relizar
    1. suma
    2. Resta
    3. Multiplicación
    4. Division
    5. salir
      ''')
    opcion = int(input('Ingrese la opción deseada '))
    if 1 <= opcion <= 4:
        
        operando1 = float(input('Ingrese operando 1 ' ))
        operando2 = float(input('Ingrese operando 2 '))
    if opcion == 1:
        print (f'La suma de {operando1} + {operando2} es {operando1+operando2}')
    elif opcion == 2:
        print (f'La resta de {operando1} - {operando2} es {operando1-operando2}')
    elif opcion == 3:
        print (f'La multiplicacion de {operando1} x {operando2} es {operando1*operando2}')
    elif opcion == 4:
        print (f'La division de {operando1} / {operando2} es {operando1/operando2}')
    elif opcion == 5:
        print('Hasta pronto!')
        salir=True
    else:
        print('Opción incorrecta')