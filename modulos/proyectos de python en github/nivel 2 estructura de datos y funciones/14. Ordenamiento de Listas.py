"""
Conceptos a Aprender:

Algoritmos de ordenamiento
Complejidad algorítmica
Comparación de algoritmos
Visualización

Implementación:

Implementar bubble sort
Implementar quick sort
Comparar rendimiento
Visualizar proceso

"""
import time
import random

# --- 1. Definición de Algoritmos (Tus Funciones) ---

# Bubble Sort (O(n^2))
def bubble_sort(lista):
    longitud_lista = len(lista)
    # Sin optimización 'intercambiado' para mantener la simplicidad
    for i in range(longitud_lista):
        for j in range(0, longitud_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Quick Sort (O(n log n))
# NOTA: Esta implementación de Quick Sort no es in-place y usa más memoria, 
# pero ilustra bien el concepto O(n log n).
'''
def Quick_sort(lista):
    # Caso base
    if len(lista) <= 1:
        return lista
    
    pivot = lista[0]
    resto_lista = lista[1:]
    
    # Metodo de comprensión de listas (Recursión)
    menores = [x for x in resto_lista if x <= pivot]
    mayores = [x for x in resto_lista if x > pivot]
    
    return Quick_sort(menores) + [pivot] + Quick_sort(mayores)
'''
# Quick sort in-place
def particion(lista,bajo,alto):
        pivot = lista[alto]
        i = bajo - 1

        for j in range(bajo,alto):
             if lista[j] <= pivot:
                  i = i + 1
                  lista[i],lista[j] = lista[j],lista[i]

        lista[i+1],lista[alto] = lista[alto],lista[i+1]
        return i + 1

def Quick_sort(lista, bajo, alto):
     if bajo < alto:
          pi = particion(lista,bajo,alto)

          Quick_sort(lista,bajo,pi-1)

          Quick_sort(lista,pi+1,alto)

# --- 2. Preparación de la Prueba ---

# Creamos una lista GRANDE (ej: 5000 elementos) para ver la diferencia de O(n^2) vs O(n log n).
# ¡Con la lista pequeña la diferencia no se nota!
TAMANO_LISTA = 5000 
lista_original = [random.randint(1, 100000) for _ in range(TAMANO_LISTA)]

# Creamos copias de la lista para asegurarnos de que ambos algoritmos 
# trabajen con datos idénticos e inicialmente desordenados.
lista_bubble = lista_original.copy()
lista_quick = lista_original.copy()
n_quick = len(lista_quick)

# --- 3. Medición de Bubble Sort ---

print(f"Iniciando Bubble Sort con {TAMANO_LISTA} elementos...")
inicio_bubble = time.time()
organizar_lista_b = bubble_sort(lista_bubble)
fin_bubble = time.time()
tiempo_bubble_sort = fin_bubble - inicio_bubble

# --- 4. Medición de Quick Sort ---

print(f"Iniciando Quick Sort con {TAMANO_LISTA} elementos...")
inicio_quick = time.time()
organizar_lista_q = Quick_sort(lista_quick, 0 , n_quick - 1)
fin_quick = time.time()
tiempo_quick_sort = fin_quick - inicio_quick


# --- 5. Resultados Finales ---

print("\n--- RESULTADOS DE LA COMPARACIÓN ---")
print(f"Bubble Sort (O(n²)): {tiempo_bubble_sort:.5f} segundos")
print(f"Quick Sort (O(n log n)): {tiempo_quick_sort:.5f} segundos")

# Opcional: una verificación rápida
# print(f"Los primeros 5 elementos de Quick Sort: {organizar_lista_q[:5]}")