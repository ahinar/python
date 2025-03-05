#funcion para saludar
print('*** Funcion para saludar ***')

#funcion si parametro\
def saludar_sin_parametro():
	print('Hola desde una funcion...')


# definimos la funcion con parametro
def saludar (nombre):
	print(f'Hola {nombre}')

# llamado de las funciones	

saludar_sin_parametro()
nombre = input('cual es tu nombre? ')

saludar(nombre)
