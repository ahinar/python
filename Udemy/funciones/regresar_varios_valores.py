print('Regresar una tupla de valores desde una funcion')

#definimos la funcion
def persona_mayusculas(nombre, apellido, edad):
    print('Esta funcion regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

#llamamos la funcion 
nombre, apellido, edad = persona_mayusculas("sandra", 'jimenez', 40)
print(f'Resultado Persona = Nombre = {nombre}, apellido = {apellido}, edad = {edad}')
