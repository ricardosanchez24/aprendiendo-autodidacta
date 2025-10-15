#reafirmar conocimientos dl proyecto 7 (contador de palabras)

#Proyecto Similar: Analizador Básico de Etiquetas HTML
import re
def analizar_HTML(texto):

    texto_minusculas = texto.lower()#manipulacion string

    texto_tokenizado = re.findall(r"<([a-z]+)>", texto_minusculas)# expresiones regulares
    
    #iniciar y contar
    contador = {}

    for etiqueta in texto_tokenizado:
        contador[etiqueta] = contador.get(etiqueta, 0) + 1#extraemos cada etiqueta y la iniciamos con un valor 0 o sumamos 1 si ya esta iniciado

    #ordenamiento

    etiqueta_total = len(texto_tokenizado)
    etiquetas_unicas = len(contador)

    comun = max(contador.items(), key=lambda item: item[1])#extraemos la etiqueta mas usada y el numero de veces usada con max

    etiqueta_max = comun[0]
    c_max = comun[1]

    print(f"el total de las etiquetas es: {etiqueta_total}")
    print(f"etiquetas unicas: {etiquetas_unicas}")
    print(f"etiqueta mas usada: {etiqueta_max} ({c_max})")

texto = "<div><p>Hola mundo</p><div><a href='#'>Link</a></div></div><p class='pie'></p>"

analizar_HTML(texto)