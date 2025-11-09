'''
16. Validador de Email
Conceptos a Aprender:

Expresiones regulares
Validación de datos
Manejo de errores
Testing

Implementación:

Definir patrón regex
Implementar validación
Probar casos
Dar feedback
'''
import re
def validar_email(email):

    patron_email = r'^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:[\-][a-zA-Z0-9]+)*\.(?:[a-zA-Z]{2,6})+$'
    verificacion_email = re.search(patron_email,email)

    if verificacion_email:
        return("email valido")
    else:
        return("email invalido, revise si cometio un error")    

email = input("ingrese su email: ")
llamada = validar_email(email)
print(llamada)