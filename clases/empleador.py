class Empleados:
    def __init__(self, nombre, apellido ):
        self.nombre = nombre
        self.apellido = apellido

class Supervisores(Empleados):
   def __init__(self, nombre, apellido, contrasena):
       super().__init__(nombre, apellido)
       self.contrasena = contrasena

class Chefs(Empleados):
    def solicitud_salida(self, days):
        return ("Puedo tomar una licencia de " + str(days)+ " days")
    
adrian = Supervisores("Adrian", "A", "Contrasena")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.solicitud_salida(3))
print(adrian.contrasena)
print(emily.nombre)