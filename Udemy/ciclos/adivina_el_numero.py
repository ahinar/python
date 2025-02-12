import random
print('Adivina el numero')
numero_secreto = random.randint(1,50)
# print (numero_secreto)

"""
#asi lo hice yo
oportunidades = 1
salir = False
numero = int(input('Ingresa un numero de 1 a 50 '))
while not salir  :
    
    if numero == numero_secreto:
        print(f'Felicitaciones adivinaste el numero en {oportunidades} oportunidades')
        salir = True
    elif oportunidades == 10:
        print(f'Agotaste las oportunidades el numero secreto erá {numero_secreto}')
        salir = True
    else:
        print(f'\nFallaste te quedan {10-oportunidades} oportunidades')
        if numero < numero_secreto:
            print("El numero secreto es mayor al ingresado")
        else:
            print("El numero secreto es menor al ingresado")
        numero = int(input('Ingresa un numero de 1 a 50 '))
        
    oportunidades += 1
    """
numero = None
oportunidades = 0
while numero != numero_secreto and oportunidades < 10:
    print(f'Adivina el numero secreto te quedan {10-oportunidades} oportunidades')
    numero = int(input('Ingresa un numero: '))
    if numero < numero_secreto:
        print('\nEl numero secreto es mayor')
    elif numero > numero_secreto:
        print('\nEl numero secreto es menor')
    
    oportunidades += 1

if numero == numero_secreto:
    print(f'Adivinaste el numero en {oportunidades} oportunidades')
else:
    print(f'Superaste la cantidad de intentos, el número secreto era {numero_secreto}')