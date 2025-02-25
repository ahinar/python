print('*** Promedio de Calificaciones ***')

#solicitamos el numero de calificaciones
numero_calificaciones = int(input('Ingrese el numero de notas a promediar: '))
lista_notas = []
for indice in range(numero_calificaciones):
    nota= float(input(f'Ingrese la nota [{indice+1}] '))
    lista_notas.append(nota)

print(f'Las notas son {lista_notas}')

#suma calificaciones con ciclo for
# suma_calificaciones = 0
# for nota in lista_notas:
#     suma_calificaciones += nota

# suma de las calificaciones con metodo sum
suma_calificaciones = sum(lista_notas)

#promedio
promedio = suma_calificaciones/numero_calificaciones
print(f'el promedio de las notas es {promedio:.2f}')