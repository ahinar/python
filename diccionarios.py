# Declara un diccionario llamado frutas que contenga al menos tres pares clave-valor,
# donde la clave sea el nombre de la fruta y el valor sea su color.
frutas={"manzana": "rojo", "naranja":"amarillo", "banano":"amarillo"}
#Usando el diccionario frutas, imprime el color de una fruta específica (por ejemplo, "manzana").
print(frutas["manzana"])
#Cambia el color de una fruta en el diccionario frutas y luego imprime el diccionario actualizado.
frutas["naranja"]="naranja"
print(frutas)
# Elimina una fruta del diccionario frutas y muestra el diccionario después de la eliminación.
del frutas["banano"]
print(frutas)
# Escribe un bucle que imprima cada fruta
# y su color en el formato "La fruta es [fruta] y su color es [color]".
for key, value in frutas.items():
    print(f"la fruta es {key} y su color es {value}")