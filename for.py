"""
palabras = input("ingrese una palabras para saber cuantas vocales tiene:\n")

contador_vocales = 0

for palabra in palabras:    
    if palabra.lower() in "aeiou":#el "in" se utiliza para ver si hay un valor dentro de otro y/o comprobar si esta un valor determinado
       contador_vocales += 1

print(f"en la palabras {palabras} hay {contador_vocales} vocales")  
"""
# 
# la funcion range()
#for i in range(0,101,2):
 #   print(i)   
 # 
#animales = ["perro", "gato", "perico", "cochino", "gallina"];

#for animal in range (len(animales)):
 #   print(animal, animales[animal])

#compras = ["pan", "arroz", "pasta", "salsa de tomate","mayonesa", #"refresco"]

#for indice, compra in enumerate(compras, start=1): #enumerate() se usa cuando se vaya a enumerar una secuencia
#    print(indice, compra)
import random
class AhorcadoAvanzado:
    def __init__(self):
        self.palabras = self.cargar_palabras()
        self.palabra_actual = None
        self.letras_adivinadas = set()
        self.vidas = 6
        self.puntuacion = 0
        self.estadisticas = {'victorias': 0, 'derrotas': 0}

    def cargar_palabras(self):
        # Aquí se cargarían las palabras desde un archivo
        return ['python', 'programacion', 'desarrollo', 'computadora']

    def iniciar_juego(self):
        self.palabra_actual = random.choice(self.palabras)
        self.letras_adivinadas = set()
        self.vidas = 6
        return self.obtener_estado()

    def obtener_estado(self):
        return {
            'palabra': ''.join(l if l in self.letras_adivinadas else '_' for l in self.palabra_actual),
            'vidas': self.vidas,
            'letras_usadas': sorted(self.letras_adivinadas),
            'puntuacion': self.puntuacion
        }

play = AhorcadoAvanzado()
estado = play.iniciar_juego()
print("Estado inicial del juego:", estado)
while play.vidas > 0 and set(play.palabra_actual) != play.letras_adivinadas:
    letra = input("Adivina una letra: ").lower()
    if letra in play.letras_adivinadas:
        print("Ya has adivinado esa letra.")
        continue
    play.letras_adivinadas.add(letra)
    if letra not in play.palabra_actual:
        play.vidas -= 1
        print(f"Letra incorrecta. Te quedan {play.vidas} vidas.")
    else:
        print("¡Letra correcta!")
    estado = play.obtener_estado()
    print("Estado actual del juego:", estado)