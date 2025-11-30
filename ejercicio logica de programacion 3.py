'''
Ejercicio de Lógica: Rotación de Elementos Tu tarea es escribir una función que tome dos argumentos:Una lista de números enteros.Un número entero $k$, que representa la cantidad de posiciones que los elementos de la lista deben ser rotados a la derecha.La función debe devolver la lista modificada (rotada).

📝 Requisitos Específicos Rotación a la Derecha: Al rotar a la derecha, el último elemento se mueve a la primera posición, y todos los demás elementos se mueven una posición a la derecha.
Ejemplo:Entrada: lista = [1, 2, 3, 4, 5], $k = 1$Salida esperada: [5, 1, 2, 3, 4] (el 5 se movió al inicio).
Ejemplo con $k > 1$:
Entrada: lista = [1, 2, 3, 4, 5], $k = 2$Salida esperada: [4, 5, 1, 2, 3]Restricción Importante: Implementa la lógica usando bucles y manipulación directa de la lista (como pop() o append(), o reconstruyendo la lista por partes). No utilices métodos avanzados de librerías como collections.deque en Python.

🤔 Pistas para PensarSi $k$ es la cantidad de rotaciones, ¿podrías hacer la rotación una posición a la vez dentro de un bucle que se repita $k$ veces?En una rotación de una posición a la derecha, el último elemento es el que tienes que guardar y luego reinsertar al inicio.¿Qué método te permite sacar (eliminar) el último elemento de una lista y almacenarlo en una variable en un solo paso? (Pista: pop())
'''
'''
def rotar_lista(lista=[] ,k=0):
    
    for i in range(k):

        ultimo_elemento = lista.pop() #elimina el ultimo elemto de la lista y lo guarda (tambien se puede guardar un elemento de una posicion deseada)
        lista.insert(0,ultimo_elemento) # inserta el elemento guardado en la posicion deseada 

    return lista

numeros = [1,2,3,4,5]
prueba = rotar_lista(numeros,1)
print(prueba)    
'''

'''
Siguiente Desafío de Lógica: Algoritmos de Búsqueda Ahora que has dominado la manipulación de cadenas y listas con bucles e índices, pasemos a un concepto fundamental en la informática: la búsqueda de datos.

Tu siguiente tarea es implementar un algoritmo de Búsqueda Lineal (o Secuencial).🔍 Ejercicio: Búsqueda Lineal Escribe una función que tome dos argumentos:Una lista de números enteros (la lista donde buscar).Un número entero (el valor que se desea buscar, $objetivo$).

La función debe recorrer la lista y devolver el índice (la posición) del primer elemento que coincida con el valor $objetivo$. 

Si el $objetivo$ no se encuentra en la lista, la función debe devolver un valor que indique que no se encontró (por ejemplo, $-1$).

📝 Requisitos EspecíficosEntrada: lista = [10, 4, 25, 8, 15], $objetivo = 8$Salida Esperada: 3 (porque el 8 está en el índice 3).Entrada (no encontrado): lista = [10, 4, 25, 8, 15], $objetivo = 99$Salida Esperada (no encontrado): -1 
Lógica Requerida: Usa un bucle for o while y una estructura condicional (if) para comparar cada elemento de la lista con el $objetivo$.
 Debes devolver el resultado inmediatamente al encontrar la primera coincidencia.¡Adelante! Este ejercicio te entrena para entender cómo los algoritmos de búsqueda recorren los datos.
'''

def algoritmo_busqueda(lista_numeros=[], numero_obj=0):
    #cantidad_lista = len(lista_numeros)
    #for i in range(cantidad_lista):
       #if lista_numeros[i] == numero_obj:
          #return i
          
    for indice, numero in enumerate(lista_numeros):

        if numero == numero_obj:
            return(indice)
    return -1
        
lista = [1,152,63,96]
prueba = algoritmo_busqueda(lista,152)  
print(prueba)              