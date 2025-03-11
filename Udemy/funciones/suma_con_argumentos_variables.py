print('***Suma con argumentos variables**')

def suma_con_for(*args):
    total = 0
    for numero in args:
        total += numero
    return total

def suma(*args):
   return sum(args)

resultado = suma_con_for(1,2,3,4,5)
print(f'la suma es: {resultado}')
print(f'la suma es: {suma(5,4,3)}')