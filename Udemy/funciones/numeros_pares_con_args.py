print('Numeros pares con args')

def numeros_pares(*args):
    for i in args:
        if i%2 == 0:
            print(f'{i} es par')
        else:
            print(f'{i} es impar')

numeros_pares(1,2,3,4,5)