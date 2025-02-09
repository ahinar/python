"""En primer lugar, la persona que quiere entrar a la casa de los espejos debe de tener más de diez años
y además no debe darte miedo la oscuridad.
Si se cumplen las condiciones anteriores, entonces podemos entrar a la casa de los espejos, de lo
contrario no vamos a poder entrar.
Y para realizar este ejemplo vamos a utilizar el operador NOT para aplicar una lógica inversa.
"""
print("***Casa delos espejos")
edad = int(input("Cual es tu edad? "))
miedo_oscuridad = input("Le temes a la oscuridad? ").lower().strip()

puede_ingresar = edad >=10 and miedo_oscuridad== "no"

if not puede_ingresar:
    print("no cumples con el regalmento de ingreso")
else:
    print("Puedes ingresar, disfruta!")
    