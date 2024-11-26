#Crea una función llamada suma_varios que acepte cualquier cantidad de números como argumentos y devuelva la suma total de esos números.
def suma_varios(*args):
    sum=0
    for x in args:
        sum+=x
    return sum

print(suma_varios(7,8,9))

print("----------------------------------------------------------\n")
# Crea una función llamada detalles_estudiante que acepte el nombre de un estudiante
# como argumento posicional y reciba información adicional (como edad, grado y ciudad)
# como argumentos nombrados. Imprime todos los detalles del estudiante.
def detelles_estudiante(nombre, **kwargs):
    print(f"nombre del estudiante: {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

detelles_estudiante("Pedro Fernandez", Edad =30, grado = 6, Ciudad= "Manizalez")

print("----------------------------------------------------------\n")
# Crea una función llamada promedio_calificaciones que acepte cualquier cantidad de calificaciones 
# como argumentos y devuelva el promedio de esas calificaciones.

def promedio_calificaciones(*args):
    suma=0
    count =0
    for nota in args:
        suma+=nota
        count+=1
    return suma/count

print(f"El promedio es {promedio_calificaciones(6,7,8,9,10)}")

print("----------------------------------------------------------\n")
# Crea una función llamada inventario que acepte una lista de productos (como args)
# y reciba información adicional sobre cada producto (como precio y cantidad) como kwargs.
# Imprime el nombre de cada producto junto con su precio y cantidad.
def inventario(*args, **kwargs):
    for producto in args:
        print(f"{producto}: ")
        if producto in kwargs:
            for clave, valor in kwargs[producto].items():
                print(f"{clave}: {valor}")
        else:
            print("No hay información disponible.")

# Llamando a la función con un diccionario para cada producto
inventario(
    "Mouse", 
    "Teclado", "Monitor",
    Mouse={"precio": 5, "cantidad": 2}, 
    Teclado={"precio": 6, "cantidad": 3},
    #Monitor={"precio": 100, "cantidad": 3}
)


