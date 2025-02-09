#verificar si se cumplio la meta
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

nombre = input("Cual es tu nombre? ")
pasos_caminados = int(input("Cuantos pasos caminaste hoy? "))

calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO

meta_cumplida = "Cumpliste" if pasos_caminados >= META_PASOS_DIARIOS else "No Cumpliste"

print(f"""{nombre}, ¡{meta_cumplida}! la meta diaria de {META_PASOS_DIARIOS} pasos,
caminaste {pasos_caminados} pasos y
quemaste {calorias_quemadas} kcl""")