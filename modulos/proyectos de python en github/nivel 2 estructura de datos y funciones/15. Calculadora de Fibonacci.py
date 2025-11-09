'''
15. Calculadora de Fibonacci
Conceptos a Aprender:

Secuencias
Memoización
Generadores
Optimización
Implementación:

Implementar Fibonacci recursivo
Implementar Fibonacci iterativo
Usar memoización
Generar secuencia
'''

def fibonacci_iterativo():
    secuenia_fibonacci = []
    
    n = int(input("ingrese un numero para la secuencia: "))
    a = 0
    b = 1
    secuenia_fibonacci.append(a)
    secuenia_fibonacci.append(b)
    if n == 0:
        return("no hay secuencia")
    elif n == 1:
        return secuenia_fibonacci[0]
    elif n == 2:
        return secuenia_fibonacci[0,1]
    elif n > 2:
        for i in range(n):
            calcular = a+b
            a = b
            b = calcular
            secuenia_fibonacci.append(calcular)
            
        return secuenia_fibonacci    

cache = {0:0, 1:1}

def fibonacci_recursivo(n):
   
    if n in cache:
        return cache[n]
    elif n >= 2:
        calcular = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)    
        cache[n] = calcular
        return calcular

numero = int(input("ingrese un numero para la secuencia: "))    
llamar = fibonacci_recursivo(numero)  
print(llamar)  