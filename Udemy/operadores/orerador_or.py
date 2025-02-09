
print("****Operador or****")
condicion1 = True
condicion2 = False
print(f"{condicion1} o {condicion1} es: ", condicion1 or condicion1)
print(f"{condicion1} o {condicion2} es: ", condicion1 or condicion2)
print(f"{condicion2} o {condicion1} es: ", condicion2 or condicion1)
print(f"{condicion2} o {condicion2} es: ", condicion2 or condicion2)

print("\n**** Prestamo libros ****")
DISTANCIA_BIBLIOTECA = 3
es_estudiante = input("Es estudiante del colegio? si/no: ").strip().upper()
#es_vecino = input("Es vecino del sector? si/no: ").strip().upper()
distancia_vivienda = int(input("A que distancia de la biblioteca vive? "))
#se_puede_prestar = es_estudiante=="si" or es_vecino == "si"
se_puede_prestar = es_estudiante=="SI" or distancia_vivienda <= DISTANCIA_BIBLIOTECA
#print(f"""La persona es estudiante ({es_estudiante}) o es vecino del sector ({es_vecino})
#se puede prestar el libro? {se_puede_prestar}""")
print(f"""La persona es estudiante ({es_estudiante}) o vive a 3 km o menos ({distancia_vivienda})
se puede prestar el libro? {se_puede_prestar}""")
