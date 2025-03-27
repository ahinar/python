print("***  Calculadora con funciones ***")

def menu():
    print('''
          --- Calculadora Basica ---
          1. suma
          2. Resta
          3. Multiplicacion
          4. division
          5. salir
    ''')
    opcion = int(input('Escoje una Opción: '))
    return opcion

def pedir_valores():
    numero1 = float(input('Ingresa el primer número: '))
    numero2 = float(input('Ingresa el segundo numero: '))
    return numero1,numero2

def hacer_operacion(opcion, salir):
   
    #pedir valores del los operandos
    if 1 <= opcion <= 4:
        numero1, numero2 = pedir_valores()
        resultado = 0
        
    if opcion == 1:
            resultado = numero1 + numero2
            print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
            resultado = numero1 - numero2
            print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
            resultado = numero1 * numero2
            print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        if numero2 != 0:
                resultado = numero1 / numero2
                print(f"El resultado de la división es: {resultado}")
        else:
                print("Error: No se puede dividir entre cero.")   
    elif opcion == 5:
            print('Saliendo del programa')
            salir = True
    else:
         print("Opción no válida.")
    return salir

if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = menu()
        salir = hacer_operacion(opcion, salir)
        
    