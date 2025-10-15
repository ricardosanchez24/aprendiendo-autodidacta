#Encontrar el número más grande: Pídele al usuario que ingrese tres números y muestra cuál es el más grande de ellos. Puedes usar una estructura if/elif/else o la función max().


#numero1 = int(input("ingrese el primer numero: \n"))
#numero2 = int(input("ingrese el segundo numero: \n"))
#numero3 = int(input("ingrese el tercer numero: \n"))

#if numero1 > numero2 and numero1 > numero3:
 #   print("el numero mayor es el primero")
#elif numero2 > numero1 and numero2 > numero3:
 #   print("el numero mayor es el segundo")
#else:
 #   print("el numero mayor es el tercero")


#Contador de vocales: Dada una cadena de texto, cuenta cuántas vocales (a, e, i, o, u) contiene

palabra = input("ingrese una palabra: \n");
contador_de_vocales = 0

for i in palabra:
    if i in "aeiou":
        contador_de_vocales += 1

print(f"en la palabras {palabra} hay {contador_de_vocales} vocales")
 

