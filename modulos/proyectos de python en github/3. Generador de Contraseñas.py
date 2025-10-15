#Descripción Cualitativa: Debes crear un generador de contraseñas que sea útil para crear contraseñas seguras, donde el usuario pueda:

#Especificar la longitud de la contraseña
#Elegir qué tipos de caracteres incluir (mayúsculas, minúsculas, números, símbolos)
#Generar múltiples contraseñas
#Ver la fortaleza de la contraseña generada
#opiar la contraseña al portapapeles El programa debe ser una herramienta práctica para crear #contraseñas seguras para diferentes servicios.

import random
import string # este modulo se utiliza para extraer los caracteres

def generar_contraseña():
    longitud_contraseña = int(input("ingrese la longitud de la contraseña deseada en un numero entero: "))
    
    caracteres = string.ascii_letters + string.digits + string.punctuation #caracteres extraido del modulo "string"
    
    #caracteres = "qwertyuiopasdfghjklñzxcvbnm.,1234567890@!#%$&" #tambien se puede hacer de esta forma sin el modulo "string" ,solo poniendo en una cadena de texto los caracteres que se quieren utilizar

    contraseña_generada = [random.choice(caracteres) for _ in range(longitud_contraseña)]
    #random.shuffle(contraseña_generada)esto se utiliza para que agarre los elementos y los ponga en orden aleatorio

    contraseña = "" .join(contraseña_generada)#se utiliza par quitar las decoraciones de la lista

    print(f"contraseña generada: {contraseña}")
    return contraseña
generar_contraseña()
