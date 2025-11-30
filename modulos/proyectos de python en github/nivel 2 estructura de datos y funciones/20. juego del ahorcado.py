# juego del ahorcado
import random
import requests
class Ahorcado:
    #constructor de la clase
    def __init__(self):
        self.palabra = self.cargar_palabra()
        self.palabra_actual = None
        self.intentos = 6
        self.letras_adivinadas = set()
        self.letras_equivocadas = set()

    #crea una funcion para hacer cada cosa consejo para POO
    #funciones de la clase
    def cargar_palabra(self):
        frases = "falta la API aqui"
        response = requests.get(frases)
        data = response.json()
        frases_api = data.get('data', [])
        if not frases_api:
            raise ValueError("No se pudieron cargar las frases desde la API.")
        
        frases_final = random.choice(frases_api)
        return set(frases_final['frase'].lower())

    def play_game(self):
        self.palabra
        self.intentos = 6
        self.letras_adivinadas = set()
        self.letras_equivocadas = set()

    def estado_juego(self):

        palabra_mostrada = ''.join([letra if letra in self.letras_adivinadas else '_' for letra in sorted(self.palabra)])

        return {
            'palabra': palabra_mostrada,
            'intentos_restantes': self.intentos,
            'letras_adivinadas': sorted(self.letras_adivinadas),
            'letras_equivocadas': sorted(self.letras_equivocadas)
        }   
        

if __name__ == "__main__":

    juego = Ahorcado()
    juego.play_game()
    estado = juego.estado_juego()
    print("Estado inicial del juego:", estado)  

    while juego.intentos > 0:
        letra = input("ingrese una letra: ").lower()

        if letra in juego.letras_adivinadas or letra in juego.letras_equivocadas:
            print("ya usaste esta letra")
            continue

        if letra in juego.palabra:
            print(f"acertaste, letra correcta")
            juego.letras_adivinadas.add(letra)
        else:
            juego.intentos -= 1
            print(f"te equivocaste letra incorrecta, te quedan {juego.intentos}")
            juego.letras_equivocadas.add(letra)        
        
        estado = juego.estado_juego()
        print("Estado actual del juego:", estado)

        if juego.letras_adivinadas == juego.palabra:
           print("¡Felicidades! Has ganado.")
           break