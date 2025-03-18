#definimos la funcion
def potencia_numero(base, exp):
    #caso base
    if exp == 0:
        resultado = 1
        return resultado
    else: #caso recursivo
        resultado_parcial = base * potencia_numero(base, exp-1)
        return resultado_parcial 
    
base = int(input('Ingresa La base de la potencia: '))
exponente = int(input('Ingresa el exponente: '))
resultado = potencia_numero(base,exponente)
print(f'la potencia de {base} exponente {exponente} es {resultado}')

