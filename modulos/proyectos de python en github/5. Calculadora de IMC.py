#Descripción Cualitativa: Debes crear una calculadora de IMC que sea útil para monitorear la salud, donde #el usuario pueda:

#Ingresar su peso y altura
#Ver su IMC calculado
#Recibir una interpretación de su resultado
#Ver recomendaciones basadas en su IMC
#Guardar un historial de sus mediciones El programa debe ser una herramienta práctica para personas #interesadas en su salud.

def calculadora_IMC():
    try:
       altura = float(input("ingrese su altura en M: "))
       peso = float(input("ingrese su peso en kg: "))

    except ValueError:
        print("Error solo puedes ingresar valores numericos")    
    
    try:
      imc = peso / altura**2 
      print(f"Su Indice de Masa Corporal es: {imc:.2f}")
    except UnboundLocalError:
        print("Error solo puedes ingresar valores numericos")
    
    try:
      if imc >= 18.5 and imc <= 24.9:
          print("Clasificacion: peso normal")
      elif imc >= 25 and imc <= 29.9:
          print("Clasificacion: sobre peso")
      elif imc >= 30:
          print("clasificacion: Obeso")
      else:
          print("Clacificacion: muy delgado")            
    except UnboundLocalError:
        print("Error solo puedes ingresar valores numericos")
calculadora_IMC()    