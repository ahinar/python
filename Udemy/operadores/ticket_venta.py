#revisar si una variable esta dentro de un rango
dato = int(input("Proporciona un dato entero: "))

#revisamos si esta dentro del rango
esta_dentro_del_rango = 1 <= dato <= 10
print(f"Variable esta dentro del rango (entre 1 y 10)? ; {esta_dentro_del_rango}")


#inverimos la logica con not
esta_fuera_del_rango = not(1 <= dato <= 10)-5
#ahora preguntamos si esta fuera del rango
print(f"Variable esta fuera del rango (entre 1 y 10)? ; {esta_fuera_del_rango}")