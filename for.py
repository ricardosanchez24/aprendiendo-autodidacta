palabras = input("ingrese una palabras para saber cuantas vocales tiene:\n")

contador_vocales = 0

for palabra in palabras:    
    if palabra.lower() in "aeiou":#el "in" se utiliza para ver si hay un valor dentro de otro y/o comprobar si esta un valor determinado
       contador_vocales += 1

print(f"en la palabras {palabras} hay {contador_vocales} vocales")  
# 
# la funcion range()
#for i in range(0,101,2):
 #   print(i)   
 # 
#animales = ["perro", "gato", "perico", "cochino", "gallina"];

#for animal in range (len(animales)):
 #   print(animal, animales[animal])

#compras = ["pan", "arroz", "pasta", "salsa de tomate","mayonesa", #"refresco"]

#for indice, compra in enumerate(compras, start=1): #enumerate() se usa cuando se vaya a enumerar una secuencia
#    print(indice, compra)