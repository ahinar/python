print('Funcion Numero par')

#definimosa la funcion
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

if __name__=='__main__':
    numero = int(input('Proporciona un numero: '))
    print(f'Es numero par? {es_par(numero)}')