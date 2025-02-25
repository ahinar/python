print('Combinacion Listas y Tuplas')
productos = [
    ('P001','Camiseta',20.0),
    ('P002','Jeans',30.0),
    ('P003','Sudadera',40.0)]

#imprimimos la informacion de cada producto y sumamos el total
valor_total = 0

#con for
# for producto in Productos:
#     print(f'Id: {producto[0]}, Descripcion: {producto[1]}, Valor: {producto[2]}')
#     valor_total += producto[2]
# print(f'El valor total de los productos es: {valor_total}')

#con for y desempaquetado
for producto in productos:
    id, descripcion, precio = producto
    print(f'Id: {id}, Descripcion: {descripcion}, Precio: ${precio}')
    valor_total += precio
print(f'El valor total de los productos es: ${valor_total}')