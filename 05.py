#bibliotecario digital: crear un programa que permita al ususario agg y buscar libros en una lista hasta que decida salir

biblioteca = ["el secreto", "la brujula", "habitos"]


def desplegar_menu():

    print("opciones menu:")

    print("1. agregar libro")
    print("2. buscar un libro")
    print("3. mostrar todos lo libros")
    print("4. salir")






def agregar_menu():

    nuevo_libro = input("agregue un libro:\n")
    
    biblioteca.append(nuevo_libro)
    print(f"el libro {nuevo_libro} a sido agregado a la lista")
    print(biblioteca)


def buscar_menu():
    buscar_libro = input("escriba que libro quiere buscar:\n")

    if buscar_libro in biblioteca: # in se utiliza pra buscar si un valor esta dentro de una estructura de datos
        
        indice = biblioteca.index(buscar_libro)
        print(f"el libro {buscar_libro} si esta en el {indice} ")
    else:
        print("el libro no esta")        


def mostrar_menu():
    print(biblioteca)



def menu_desplegado():
    
    while True:

        desplegar_menu()

        usuario = int(input("elija una opcion: "))

        if usuario == 1:
            agregar_menu()
        elif usuario == 2:
            buscar_menu()
        elif usuario == 3:
            mostrar_menu()
        elif usuario == 4:
            print("saliendo del programa")
            break
        else:
            print("el numero ingresado no es valido, elija una opcion del 1 al 4")


          

menu_desplegado()