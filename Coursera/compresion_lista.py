data = [2,3,5,7,11,13,17,19,23,29,31]
print(data)

# Ex1: List comprehension: actualizando la misma lista
data = [x+3 for x in data]
print("Actualizando la lista sumando 3 a cada item: ", data)

# Ex2: List comprehension: creando una lista diferente con los valores actualizados
new_data = [x*2 for x in data]
print("Creando una nueva lista:  ", new_data)

# Ex3: Con una if-condition: multiplos de cuatro:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible por cuatro", fourx)

# Ex4: Alternativamente, también podemos actualizar la lista con la condición if.
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible por cuatro menos 1: ", fourxsub)

# Ex5: Usando la funcion rango:
nines = [x for x in range(100) if x%9 == 0]
print("Nueves: ", nines)

print("\n----------------------------------------------------------------\n")
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)