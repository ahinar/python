class A:
    def __init__(self,c):
        print("---------Inside class A----------")
        self.c = c
    print("Print dentro de A")

    def alpha(self):
        c = self.c +1
        return c
    
print(dir(A))
print("Instaciando A..")
a = A(1)
#print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Dentro class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instanciando B..")
b = B(a)
print(a)