#crear clase
class Aritmetica:
    #creamos los atributos
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        suma = self.operando1 + self.operando2
        print(f'{self.operando1} + {self.operando2} = {suma}')
    def restar(self):
        resta = self.operando1-self.operando2
        print(f'{self.operando1} - {self.operando2} = {resta}')
    def multiplicar_dividir(self):
        multiplicar = self.operando1*self.operando2
        dividir = self.operando1/self.operando2
        print(f'{self.operando1} * {self.operando2} = {multiplicar}')
        print(f'{self.operando1} / {self.operando2} = {dividir:.2f}')
    
if __name__ == '__main__':
    print('Objeto 1')
    aritmetica1 = Aritmetica(5,7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar_dividir()
    print('Objeto 2')
    aritmetica2 = Aritmetica(12,16)
    aritmetica2.sumar()
    aritmetica2.restar()
    print('Objeto 3')
    aritmetica3 = Aritmetica(3)
    aritmetica3.operando2 = 3
    aritmetica3.sumar()
    print('Objeto 4')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 =5
    aritmetica4.operando2 = 4
    aritmetica4.sumar()
    print('Objeto 5')
    aritmetica5 = Aritmetica(operando2=5, operando1=6)
    aritmetica5.sumar()



