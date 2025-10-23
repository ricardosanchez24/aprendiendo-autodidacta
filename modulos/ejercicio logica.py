#enunciado
#Escribe una función o programa que reciba una cadena de texto (una palabra o frase) y determine si es un #palíndromo.

#Un palíndromo es una palabra o expresión que se lee igual de izquierda a derecha que de derecha a #izquierda.

import re

class texto_invertido:

    def __init__(self, texto):
        self.texto = texto.strip().lower()

    def limpiar_texto(self):
        texto_limpio = re.sub(r'[^a-zA-Z0-9]', "", self.texto).strip().lower()
        return texto_limpio

    def palindromo(self, texto_limpio=None):
        if texto_limpio is None:
            texto_limpio = self.limpiar_texto()
        cadena_invertida = texto_limpio[::-1]

        if texto_limpio == cadena_invertida:
            return True
            
        else:
            return False
        
        
        

frase = "oso"
obj = texto_invertido(frase)
resultado = obj.palindromo()