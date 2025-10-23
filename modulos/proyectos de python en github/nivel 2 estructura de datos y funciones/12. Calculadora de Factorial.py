#crear una calculadora factorial con recursividad

class factorial:
    def __init__(self, numero):
        self.numero = numero

    def p_factorial(self):
        if self.numero == 0 or self.numero == 1:
            return 1
        
        return self.numero * factorial(self.numero - 1).p_factorial()

    def verifiacion_numero(self):
        if self.numero >= 0:
            return self.p_factorial()
        else:
            return "solo se puede realizar la factorizacion en numeros enteros no negativos"
try:
  n = int(input("ingrese el numero: "))
  inicio = factorial(n).verifiacion_numero()
  print(inicio)
except ValueError:
    print("el numero ingresado es invalido, ingrese un numero entero")  
#isinstance(self.numero, int) and