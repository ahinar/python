
#reserva de hotel
tarifa_cuarto_vista_mar = 190.50
tarifa_cuarto_sin_vista = 150.50
nombre = input("Cual es tu Nombre ").strip().upper()
dias_estadia = int(input("Cuantos días te quedaras en nuestro Hotel "))
cuarto_con_vista_mar = input("Deseas cuarto con vista al mar? (si/no) ").strip().lower()
vista_al_mar =  cuarto_con_vista_mar == "si"
#vista_al_mar = True if cuarto_con_vista_mar == "si" else False
tarifa = tarifa_cuarto_vista_mar * dias_estadia if cuarto_con_vista_mar == "si" else tarifa_cuarto_sin_vista * dias_estadia

print(f"""Hola {nombre} tu tarifa por quedarte {dias_estadia} dias es de {tarifa}
Tu cuarto tiene vista al mar: {vista_al_mar}""" )
