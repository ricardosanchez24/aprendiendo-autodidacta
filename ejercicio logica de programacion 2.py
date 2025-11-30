'''
Ejercicio de Lógica: Suma de Pares e Impares Tu tarea es escribir una función que reciba una lista de números enteros y devuelva dos resultados:La suma total de todos los números pares encontrados en la lista.La suma total de todos los números impares encontrados en la lista.

📝 Requisitos Específicos Entrada: Una lista o array de números enteros (ejemplo: [1, 5, 8, 12, 7, 4]).Salida: Un mecanismo para mostrar dos valores: la suma de los pares y la suma de los impares. (Para el ejemplo anterior: Pares = $8 + 12 + 4 = 24$; Impares = $1 + 5 + 7 = 13$).

Lógica Requerida: Debes utilizar un bucle (for o while) para recorrer la lista y una estructura condicional (if/else) para determinar si cada número es par o impar.

🤔 Pista Clave Para saber si un número es par o impar, usa el operador módulo (o residuo), que en la mayoría de los lenguajes es % .Si un número dividido por 2 tiene un residuo de 0 (número % 2 == 0), es par.Si el residuo es diferente de 0, es impar.
'''

def suma_par_impar():
    lista_numeros = [5,4,8,9,63,25,125,7,2,3,1]
    suma_impar = 0
    suma_par = 0
    for i in lista_numeros:
        if i % 2 == 0:
            suma_par += i 
        else:
            suma_impar += i 
    return suma_par, suma_impar

prueba = suma_par_impar()
print(prueba)