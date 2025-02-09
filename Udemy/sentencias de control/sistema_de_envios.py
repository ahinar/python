ENVIO_NACIONAL = 10 #costo por kilo
ENVIO_INTER = 20

print ("*** Sistema de Envios ***\n")
destino = input("Su destino es nacional o Internacional? ").strip().lower()
peso = int(input("Cual es el peso de su articulo en KG? "))

if destino == "nacional":
    tarifa = peso * ENVIO_NACIONAL
elif destino == "internacional":
    tarifa = peso * ENVIO_INTER
else:
    print("Destino desconocido")

if tarifa is not None:
    print(f"La tarifa de su envio {destino} es ${tarifa}")