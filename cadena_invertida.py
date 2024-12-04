# sintaxis
# cadena[inicio:parar:paso]
# str[star:stop:step]

cadena= "ejemplo"
nueva_cadena = cadena[::-1]
print(nueva_cadena)

def cadena_invertida(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena_invertida(cadena[1:])+cadena[0]

cadena2="ejemplo"  
invertida=cadena_invertida(cadena2)
print(invertida)