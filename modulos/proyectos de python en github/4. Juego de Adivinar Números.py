#Descripción Cualitativa: Debes crear un juego divertido y adictivo donde el usuario:

#Intente adivinar un número secreto
#Reciba pistas si está cerca o lejos
#Vea cuántos intentos lleva
#Pueda jugar múltiples rondas
#Vea su puntuación y récord El juego debe ser entretenido y mantener al usuario interesado en seguir #jugando.
import random
print("bienvenido al juego de adivinar el numero entre 1 y 100")
numero_aleatorio = random.randint(1,100)
intentos = 1
while True:
    try:
        numero_usuario = int(input(f"intento (presiona 0 para salir) {intentos}: "))
    except ValueError :
        print("Error, ingresa un numero entero")
        continue

    if numero_usuario == 0:
        print("programa cerrado")
        print(f"hiciste {intentos} intentos")
        break
    elif numero_usuario > 100:
        print("solo puedes ingresar numero entre 1 y 100")
        continue
    
    elif numero_usuario == numero_aleatorio:
        print(f"Felicidades acertaste!!! El numero random es: {numero_aleatorio}")
        print(f"lo lograste en  {intentos} intentos")
        break
    elif numero_usuario > numero_aleatorio:
        print("demasiado alto")
        intentos += 1
        
    elif numero_usuario < numero_aleatorio:
        print("demasiado bajo")
        intentos += 1
        
                           