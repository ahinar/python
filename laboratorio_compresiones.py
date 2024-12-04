# Datos de entrada: Lista de diccionarios
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Función que se pasará a la función map(). No cambies esto.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifica la lista de diccionarios de empleados en una lista de cadenas de nombre-departamento

   [IMPLEMENTAR ME] 
      1. Usa el método map() para aplicar mod() a todos los elementos en employee_list

   Args:
      employee_list: lista de objetos de empleados

   Returns:
      list - Una lista de cadenas que consisten en nombre + departamento.
   """
   ### ESCRIBE EL CÓDIGO DE LA SOLUCIÓN AQUÍ
   map_emp= (map(mod, employee_list))
   return list(map_emp)
   raise NotImplementedError()

def generate_usernames(mod_list):
   """ Genera una lista de nombres de usuario 

   [IMPLEMENTAR ME] 
      1. Usa la comprensión de listas y la función replace() para reemplazar los caracteres de espacio
         con guiones bajos

      La comprensión de listas se ve así:
      list = [ function() for <item> in <list> ]

      El formato para la función replace() es:

      test_str.replace(“a”, “z”) # reemplaza cada “a” en test_str con “z”

   Args:
      mod_list: lista de cadenas de nombre-departamento

   Returns:
      list - Una lista de nombres de usuario que consisten en nombre + departamento delimitados por guiones bajos.
   """
   ### ESCRIBE EL CÓDIGO DE LA SOLUCIÓN AQUÍ

   lista1 = [x.replace(" ", "_") for x in mod_list ]
   return list(lista1)

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Mapea el id del empleado a la primera inicial

   [IMPLEMENTAR ME] 
      1. Usa la comprensión de diccionarios para mapear el id de cada empleado (valor) a la primera letra de su nombre (clave)

      La comprensión de diccionarios se ve así:
      dict = { key : value for <item> in <list> }

   Args:
      employee_list: lista de objetos de empleados

   Returns:
      dict - Un diccionario que mapea el id de un empleado (valor) a su primera inicial (clave).
   """
   ### ESCRIBE EL CÓDIGO DE LA SOLUCIÓN AQUÍ
   dict_inicial = {x["name"][0]: x["id"] for x in employee_list}
   return dict_inicial

   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Lista de empleados modificada: " + str(mod_emp_list) + "\n")

   print(f"Lista de nombres de usuario: {generate_usernames(mod_emp_list)}\n")

   print(f"Iniciales e ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()
