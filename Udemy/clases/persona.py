#crear clase persona
class Persona:
    #creamos los atributos
    def inicializar_persona(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona
              Nombre: {self.nombre}
              Apellido: {self.apellido}\n
''')

#creacion de objeto
if __name__ == "__main__":
    #creacion de primer objeto
    persona1= Persona()#crea un objeto vacio en memoria
    persona2= Persona()
    persona1.inicializar_persona('Fernando', 'Gonzalez')
    persona2.inicializar_persona('Maria', 'Gonzalez')

    persona1.mostrar_persona()
    persona2.mostrar_persona()

    