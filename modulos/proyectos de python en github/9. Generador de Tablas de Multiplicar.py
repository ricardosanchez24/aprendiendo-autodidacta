#tablas de multiplicar

#numero_multiplicacion = int(input("ingresa la tabla: "))

#for i in range(1,11):
 #   multiplicacion = i * numero_multiplicacion
 #   print(f"{i} x {numero_multiplicacion} = {multiplicacion}")

# con bucles anidados
 #el primer bucle toma a y solo lo cambia cuando se haya ejecutado todo el bucle interno
#for i in range(1,10):
    # el segundo bucle (interno) toma el rango el multiplica a x b e imprime el resultado
  #  for j in range(1,10): 
  #      multipicacion = i * j
  #      print(f"{i} x {j} = {multipicacion}")

#ejercicio triangulos

for i in range(1,6):
    for j in range(i):
       print(f"*",end=" ")
    print()
       