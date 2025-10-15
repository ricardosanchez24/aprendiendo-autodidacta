mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

mi_lista += [6, 7, 8, 9]

print(mi_lista)

mi_lista.append(195)
print(mi_lista)

mi_lista[5] = 24
print(mi_lista)

print(mi_lista[3])

mi_lista[2:5] = ""
print(mi_lista)

print(mi_lista[1:3])

print(len(mi_lista))

lista_anidada = [
    [1, 2, 3],                # Lista de enteros
    ["a", "b", "c"],          # Lista de cadenas
    [True, False, True]       # Lista de booleanos
]
print(lista_anidada[2] [0])