import re

def contar_palabras(texto):
    palabras = texto.lower()#pasamos el texto a minusculas
    palabras_sinPuntuacion = re.sub(r"[^\w\s]", " ", palabras)#usamos el patron \w\s (signos y espacios) y lo reemplaza con un espacio (" ")
    palabras_tokenizadas = re.findall(r"\w+",palabras_sinPuntuacion)#aqui separamos las palabras y las tokemizamos
    contador = {}

    for palabra in palabras_tokenizadas:
        contador[palabra] = contador.get(palabra,0) + 1
    
    
    item_comun = max(contador.items(), key=lambda item: item[1])

    palabra_comun = item_comun[0]
    conteo_comun = item_comun[1]

    total_palabras = len(palabras_tokenizadas)

    palabras_unicas = len(contador)

    print(f"total de palabras: {total_palabras}")
    print(f"palabra unica: {palabras_unicas}")
    print(f"palabra mas comun: {palabra_comun} ({conteo_comun})")



palabras = input("ingresa la oracion para contar sus palabras:\n")

contar_palabras(palabras)



#texto = input("Introduce un texto: ")
#resultado = contar_palabras(texto)
#print(resultado)