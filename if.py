#if
#pedir las notas

#calificacion = int(input("ingrese la calificacion:\n"));

#if calificacion == 20:#
  #  print("muy sobresaliente")
#elif calificacion  >= 18:#
  #  print("excelente")  
#elif calificacion >= 15:#
  #  print("bien")
#elif calificacion >= 12:
#    print("hay que mejorar")
#elif calificacion >= 10:
  #  print("mal, apenas pasaste")
#else:
  #  print("reprobado")      
  # 
  # ejercicio año bisiesto
año = int(input("agregue el año par saber si es bisiesto o no:\n"))

if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")    