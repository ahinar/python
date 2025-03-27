print('Calculadora impuesto')

def calcular_impuesto(pago, impuesto):
    pago_total= pago + pago*(impuesto/100)
    return pago_total

def solicitar_info():
    pago = float(input('Ingrese el monto a pagar sin impuestos: '))
    impuesto = float(input('Ingrese el valor del impuesto: '))
    return pago, impuesto

# pago = float(input('Ingrese el monto a pagar sin impuestos: '))
# impuesto = float(input('Ingrese el valor del impuesto: '))
pago, impuesto = solicitar_info()
pago_total = calcular_impuesto(pago, impuesto)
print(f'El pago total es {pago_total}')