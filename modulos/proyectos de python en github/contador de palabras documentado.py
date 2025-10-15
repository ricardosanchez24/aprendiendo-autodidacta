#generar una lsita con cosas aleatorias

#import random
#texto = "holfjt"
#numero_random = random.choices(texto)

#print(numero_random)

# Importamos el módulo de expresiones regulares para limpieza y tokenización
import re

# Definimos la función principal que procesa el texto
def contar_palabras(texto):
    # --- PASO 1: LIMPIEZA Y NORMALIZACIÓN ---

    # Convertimos todo el texto a minúsculas
    palabras = texto.lower()
    
    # Eliminamos la puntuación usando re.sub()
    # El patrón r"[^\w\s]" busca cualquier carácter que NO sea una palabra (\w) o espacio (\s)
    # y lo reemplaza con un espacio (" ") para evitar que las palabras se peguen
    palabras_sinPuntuacion = re.sub(r"[^\w\s]", " ", palabras)
    
    # --- PASO 2: TOKENIZACIÓN ---

    # Usamos re.findall() con el patrón r"\w+"
    # Esto busca y extrae todas las secuencias de uno o más caracteres de palabra
    # El resultado es una lista limpia de palabras
    palabras_tokenizadas = re.findall(r"\w+", palabras_sinPuntuacion)
    
    # --- PASO 3: CONTEO DE FRECUENCIA (Diccionarios) ---

    # Inicializamos un diccionario para almacenar las frecuencias de cada palabra
    contador = {}

    # Recorremos la lista de palabras tokenizadas
    for palabra in palabras_tokenizadas:
        # Usamos el método .get() del diccionario
        # Si la palabra existe, sumamos 1 a su conteo; si no existe, la inicializamos a 1
        contador[palabra] = contador.get(palabra,0) + 1
    
    # --- PASO 4: CÁLCULO DE ESTADÍSTICAS ---
    
    # Encontramos la palabra más común (el ítem con el valor más alto)
    # Usamos max() con una función lambda que le indica ordenar por el valor (item[1])
    item_comun = max(contador.items(), key=lambda item: item[1])

    # Desempaquetamos la tupla resultante del item más común
    palabra_comun = item_comun[0]
    conteo_comun = item_comun[1]

    # Calculamos el total de palabras usando la longitud de la lista tokenizada
    total_palabras = len(palabras_tokenizadas)

    # Calculamos el número de palabras únicas usando la longitud del diccionario de conteo
    palabras_unicas = len(contador)

    # --- PASO 5: SALIDA ESPERADA ---
    
    # Imprimimos todas las estadísticas finales
    print(f"total de palabras: {total_palabras}")
    print(f"palabra unica: {palabras_unicas}")
    print(f"palabra mas comun: {palabra_comun} ({conteo_comun})")

# --- BLOQUE DE EJECUCIÓN ---

# texto_ejemplo = "Python es genial, y Python es muy usado en el mundo Python. Python!"
# contar_palabras(texto_ejemplo)
    

