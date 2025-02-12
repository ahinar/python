print('Validacion contraseña')
contrasena = input("ingresa una contraseña de 6 caracteres ").strip()
while len(contrasena) < 6:
    print('La contraseña no cumple con lo solicitado')
    contrasena = input("ingresa una contraseña de 6 caracteres ").strip()        
else:
    print('Contraseña generada con exito')
        

