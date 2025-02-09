#generador email
print("*********Generador de email***********")
nombre = input("Ingresa tu nombre: ").lower().replace(" ",".").strip()
apellidos = input("Ingresa tu apellido: ").lower().replace(" ",".").strip()
dominio = "@global.mentoring.com"
email = nombre+"."+apellidos+dominio
print(f"tu email corporativo es: {email} ")