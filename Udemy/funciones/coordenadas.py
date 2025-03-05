print('obtener coordedadas x, y,z')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

#llamar funcion
resultado = obtener_coordenadas()
print(resultado)# imprime una tupla

#unpaking tupla
x1, y2, z2 = resultado

print(f'x = {x1}, y = {y2}, z = {z2}')