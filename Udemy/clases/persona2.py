#crear clase persona
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'''Persona
              Nombre: {self.nombre}
              Apellido: {self.apellido}
              Direccion de mem. de self: {id(self)}
              Direccion Hexadecimal: {hex(id(self))}

''')

if __name__ == '__main__':
    # creamos un objeto
    persona1 = Persona('Lila', 'Gonzalez')
    persona1.mostrar_persona()
    # mostramos la direccion de memoria del objeto
    print(f'Direccion de mem. de persona1: {id(persona1)}')
    print(f'Direccion Hexadecimal: {hex(id(persona1))}')

    #creamos un segundo objeto
    persona2 = Persona('Wlfrand', 'Linares')
    persona2.mostrar_persona()