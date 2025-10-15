while True:    
     numero1 = int(input("ingrese el primer numero: "))
     numero2 = int(input("ingrese el segundo numero: "))
     operacion = input("ingrese la operacion a realizar(+, -, *, /) presione 0 para salir:\n")
     
     if operacion == "+":
         resultado = numero1 + numero2
         print(f"el resultado de {operacion} es: {resultado}")
      
     elif operacion == "-":
         resultado = numero1 - numero2
         print(f"el resultado de {operacion} es: {resultado}")
     
     elif operacion == "*":
         resultado = numero1 * numero2
         print(f"el resultado de {operacion} es: {resultado}")
     
     elif operacion == "/":
         if numero2 != 0:
          resultado = numero1 / numero2
          print(f"el resultado de {operacion} es: {resultado:.2f}")
         else:
             print("error, no se puede dividir entre 0") 
     elif  operacion == "0":
         break
     else:
     
         print("Error, ingrese un signo de opracion (+,-,*,/)")                