#validar usuario con and
#constantes con los valores correctos
USUARIO = "Usuario"
PASWORD = "12345"

usuario = input("Ingrese su Usuario: ").strip().lower()
pasword = input('Ingrese su Contraseña: ').strip().lower()

resultado = USUARIO == usuario and PASWORD == pasword
print(usuario)
print(f"Sus credenciales son correctas = {resultado}")