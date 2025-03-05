print('***Funcion con Argumentos por nombre ***')

def imprimir_persona(nombre= '', apellido= '', edad =0):
    print(f'Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')

#primero llamamos a la funcion pasando los argumentos de manera posicional
imprimir_persona("Ricardo", 'Quintana', 32)
#llamar la funcion usando argumentos por nombre sin importar el orden
imprimir_persona(apellido='Rojas', nombre='Carlos', edad=28)
#llamar funcion con valores por defaULT
imprimir_persona()
imprimir_persona(nombre='Carlos')
imprimir_persona(apellido='Gonzalez', nombre='Fernando')

