print("****Operador and****")
condicion1 = True
condicion2 = False
print(f"{condicion1} y {condicion1} es: ", condicion1 and condicion1)
print(f"{condicion1} y {condicion2} es: ", condicion1 and condicion2)
print(f"{condicion2} y {condicion1} es: ", condicion2 and condicion1)
print(f"{condicion2} y {condicion2} es: ", condicion1 and condicion2)


print("\n****Descuento tienda****")
# descuento 10% de tienda si es cliente inscrito y lleva mas de 10 articulos
NUM_ARTICULOS_DESCUENTO =10
cantidad_articulos = int(input("Cuantos articulos lleva? "))
menbresia = input("Tiene menbresia? si/no ").strip().lower()
tiene_descuento= cantidad_articulos >= NUM_ARTICULOS_DESCUENTO and menbresia == "si"
print (f"El cliente tiene descuento: {tiene_descuento}")