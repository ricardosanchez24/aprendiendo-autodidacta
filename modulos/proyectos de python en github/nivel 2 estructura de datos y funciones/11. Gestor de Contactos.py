import json
import re
#paso 0: menu
#paso 1 : agg usuario
#paso 2 : modificar usuario
#paso 3 : eliminar usuario
#paso 4 : mostrar usuario
#paso 5 : listar usuarios
#paso 6 : salir JSON
# Inicialización
contactos = {}

# Bloque de Definición de Funciones Operativas

def cargar_contactos():
    try:
        with open("contactos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_contactos():
    global contactos # "global" se utiliza para cambiar el valor del tipo de dato global (diccionario en este caso) solo dentro de esta funcion y no alterar su alor afuera ni para crear una variable en la funcion con ese nombre
    with open("contactos.json", "w") as archivo:
        json.dump(contactos, archivo, indent=4)

def agregar_contactos():
    global contactos
    nombre = input("ingrese el nombre del contacto: ").strip().lower()
    if not nombre:
        print("agrege un nombre valido")
        return
    try:
        telefono = int(input("ingrese el numero de telefono: "))
    except ValueError:
        print("Entrada invalida, ingrese un numero de telefono valido")
        return
    email = input("ingrese su email: ").strip()
    estructura_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    conincidencia = re.match(estructura_correo,email)
    if not conincidencia :
        print("formato de email invalido")
        return
    
    categoria = input("ingresa su categoria: ").strip()
    nota = input("ingresa una nota(ejem: cumpleaños x dia): ").strip()

    contactos[nombre] = {
        "telefono": telefono,
        "email": email,
        "categoria": categoria,
        "nota": nota
    }
    print(f"Contacto '{nombre}' agregado correctamente.")

def modificar_contacto():
    global contactos
    nombre = input("ingrese el contacto a modificar: ").strip().lower()
    if nombre not in contactos:
        print("el contacto no existe")
        return

    # Telefono: permitir dejar vacío para no cambiar
    while True:
        nuevo_telefono_str = input("Ingrese el nuevo número de teléfono. Deje vacío para no cambiar: ").strip()
        if not nuevo_telefono_str:# este pedazo de codigo funciona para decirle al programa que si no se lleno el campo entonces deje el valor anterior y que siga con la ejecucion
            break
        try:
            nuevo_telefono = int(nuevo_telefono_str)
            contactos[nombre]['telefono'] = nuevo_telefono
            break
        except ValueError:
            print("Entrada inválida. Ingrese solo dígitos.")

    nuevo_email = input("ingrese el nuevo email (deje vacío para no cambiar): ").strip()
    if nuevo_email:
        if "@" not in nuevo_email and "." not in nuevo_email:
            print("Error, el email le falta @ o .")
            return
        contactos[nombre]["email"] = nuevo_email

    nueva_categoria = input("ingrese la nueva categoria (deje vacío para no cambiar): ").strip()
    if nueva_categoria:
        contactos[nombre]["categoria"] = nueva_categoria

    nueva_nota = input("ingrese la nueva nota (deje vacío para no cambiar): ").strip()
    if nueva_nota:
        contactos[nombre]["nota"] = nueva_nota

    print(f"Contacto '{nombre}' modificado correctamente.")

def eliminar_contacto():
    global contactos
    eliminar = input("ingrese el contacto a eliminar: ").strip().lower()
    if eliminar in contactos:
        del contactos[eliminar]
        print(f"✅ Contacto '{eliminar}' eliminado correctamente.")
    else:
        print(f"❌ Error: El contacto '{eliminar}' no se encuentra en la lista.")

def mostrar_usuario():
    usuario_mostrar = input("ingrese el ususario a mostrar: ").strip().lower()
    if usuario_mostrar in contactos:
        print(f"el usuario, {usuario_mostrar} tiene los siguientes datos: ")
        print(f"telefono: {contactos[usuario_mostrar]["telefono"]} " )
        print(f"email:  {contactos[usuario_mostrar]["email"]}")
        print(f"categoria: {contactos[usuario_mostrar]["categoria"]}")
        print(f"nota: {contactos[usuario_mostrar]["nota"]}")
    else:
        print("el usuario no existe")

def listar_todos_usuarios():
    if contactos:
        for nombre, datos in contactos.items():
            print(f"{nombre}: {datos}")
    else:
        print("No hay contactos registrados.")

# Bloque del Menú y Ejecución Principal

def mostrar_menu():
    print("\n---menu---\n")
    print("1. Agregar contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar contacto")
    print("5. Listar contactos")
    print("6. Guardar y salir")

def ejecutar_programa():
    global contactos
    # Cargar contactos al inicio del programa (después de definir la función)
    contactos = cargar_contactos()

    while True:
        mostrar_menu()
        opcion = input("ingrese una opcion: ").strip().lower()

        if opcion == "1":
            agregar_contactos()
        elif opcion == "2":
            modificar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            mostrar_usuario()
        elif opcion == "5":
            listar_todos_usuarios()
        elif opcion == "6":
            guardar_contactos()
            print("Contactos guardados. Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Punto de Entrada (Final)
ejecutar_programa()