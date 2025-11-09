'''
Tu tarea: Reescribe las líneas 4, 5 y 6 (el bucle for y la condición if) en una sola comprensión de lista que asigne el resultado a la variable longitudes_largas.
'''
'''
frase = "Las comprensiones de lista son poderosas y concisas"
palabras = frase.split()
'''
'''
for palabra in palabras:
    if len(palabra) >= 5:
        longitudes_largas.append(len(palabra))

print(longitudes_largas)
'''
'''
longitudes_largas = [len(x) for x in palabras if len(x) >= 5 ]
print(longitudes_largas)
'''

'''
Necesitas crear una lista que contenga todos los múltiplos de 7 en el rango del 1 al 100 (incluyendo el 7 y el 100 si fuera múltiplo).

Tu tarea: Utiliza una comprensión de lista para crear la lista multiplos_de_7.

Pista: Usa la función range(1, 101) y el operador módulo (%).
'''
multiplos_7 = [x for x in range(1,101) if x % 7 == 0 or x == 100]
print(multiplos_7)