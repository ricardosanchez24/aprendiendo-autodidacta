import random

class juego_dados:

    def __init__(self,usuario):
        self.usuario = usuario
        self.puntuacion = 0

    def juego(self):    

        self.intento1 = random.randint(1,6)
        self.intento2 = random.randint(1,6)
        resultado_mano = self.intento1 + self.intento2

        self.puntuacion += resultado_mano
        
        print (f"{self.usuario}: {self.intento1}, {self.intento2}. Resultado final: {resultado_mano}")
        return self
    
    def __gt__(self,otro_usuario):
        if not isinstance(otro_usuario,juego_dados): # manejo de error, verifica si es una instancia o no
            return NotImplemented
        return self.puntuacion > otro_usuario.puntuacion #comparacion
    
    def __repr__(self):
        return f"{self.usuario}: {self.puntuacion} puntos"

        
jugador1 = juego_dados("mario").juego()
print(jugador1)

jugador2 = juego_dados("maria").juego()
print(jugador2)

jugador3 = juego_dados("juan").juego()
print(jugador3)

jugador4 = juego_dados("carlos").juego()
print(jugador4)

lista_jugadores = [jugador1, jugador2]

lista_jugadores.append(jugador3)
lista_jugadores.append(jugador4)

ganador = max(lista_jugadores)

print(f"el ganador es {ganador.usuario}")
