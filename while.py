import random

numero_aleatorio = random.randint(1,100)



while True:
    numero_usuario = int(input("ingrese el numero: "))

    if numero_usuario == numero_aleatorio:
        break #break funciona para detener un bucle infinito o un condicional cuando una condicion de cumpla, se utiliza para detener bucles,condicionales,etc
    elif numero_usuario > numero_aleatorio:
        print("el numero ingresado es alto")
    else:
        print("el numero ingresado es bajo")

print(f"felicidades adivinaste el numero random de {numero_aleatorio}")