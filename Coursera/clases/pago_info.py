class Payslips:
    def __init__(self, nombre, pago, importe) -> None:
        self.nombre = nombre
        self.pago = pago
        self.importe = importe

    def pay(self):
        self.pago = "si"

    def status(self):
        if self.pago == "si":
            return self.nombre + " esta pago $" + str(self.importe)
        else:
            return self.nombre + " aun no esta pago"
        
pedro = Payslips("Pedro", "no", 1000)
juan = Payslips("Juan", "no", 3000)

print(pedro.status(), "\n", juan.status())

pedro.pay()
print("despues de pagar")
print(pedro.status(), "\n", juan.status())

