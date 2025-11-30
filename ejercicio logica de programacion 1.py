'''
Ejercicio de Lógica: Inversión de Cadena
Tu tarea es escribir una función o programa que tome una cadena de texto (un string) como entrada y devuelva una nueva cadena con los caracteres en orden inverso.

 Requisitos Específicos Entrada: Una cadena de texto cualquiera (ejemplo: "programacion").Salida: Una nueva cadena con los caracteres de la entrada en orden inverso (ejemplo: "noicamargorp").Restricción (Importante): Intenta no utilizar las funciones nativas o métodos de alto nivel que tu lenguaje de programación pueda tener para invertir cadenas directamente (como reverse() en JavaScript o Python, por ejemplo). La idea es que implementes la lógica paso a paso, usando bucles (for, while) y la manipulación de índices o la construcción de la nueva cadena.
 
 🤔 Pistas para Pensar ¿Cómo puedes recorrer la cadena original empezando por el final?¿Cómo puedes ir añadiendo cada carácter a una nueva cadena vacía?Recuerda que en la mayoría de los lenguajes, si una cadena tiene $N$ caracteres, el índice del primer carácter es 0 y el índice del último carácter es $N-1$.
'''

def invertir_cadena(cadena_texto="hola"):
    cadena_invertida = []

    for letra in cadena_texto[::-1]:
        cadena_invertida.append(letra)
        
    print(cadena_invertida)
    

while True:
    cadena_a_invertir = input('ingrese una palabra a invertir: ').lower().strip()
    if not any(char.isdigit() for char in cadena_a_invertir):
        break  # Salir del bucle si no hay dígitos
    else:
        print("Error: Por favor, no incluyas números.")


invertir_cadena(cadena_a_invertir)    