import json

"""
programa de gestion de biblioteca de libros
1-agg libro -
2-modificar libro -
3-eliminar libro -
4-mostrar libro -
5-listar libros -
6-guardar y salir -
7- menu
"""
class biblioteca:
    def __init__(self):
        self.libros = {}

    def cargar_libros(self):
        try:
            with open("biblioteca.json", "r") as archivo:
                self.libros = json.load(archivo)
        except FileNotFoundError:
            self.libros = {}        
    
    def guardar_salir(self):
        with open("biblioteca.json", "w") as archivo:
            json.dump(self.libros, archivo)    

    def agg_libro(self):
        titulo = input("ingrese el titulo del libro: ").strip().lower()
        if titulo in self.libros:
            return("el libro ya existe en la biblioteca")
            
        autor = input("ingrese el autor del libro: ").strip().lower()
        descripcion = input("ingrese una descripcion del libro: ").strip().lower()
        año = int(input("ingrese el año del libro: "))
        id = int(input("ingrese el id del libro: "))
       
        self.libros[titulo] = {
            "descripcion": descripcion,
            "autor": autor,
            "año": año,
            "id": id
        }
        return(f"El libro '{titulo}' ha sido agregado exitosamente a la biblioteca.")

    def  modificar_libro(self):
        titulo_modificar = input("ingrese el titulo del libro a modificar: ").strip().lower()
        if titulo_modificar not in self.libros:
            return(f"Error: el libro '{titulo_modificar}' no se encuentra en la biblioteca.")

        autor = input("ingrese el nuevo autor del libro: ").strip().lower()
        año = int(input("ingrese el nuevo año del libro: "))
        id = int(input("ingrese el nuevo id del libro:"))
        descripcion = input("ingrese la nueva descripcion del libro: ").strip().lower()

        self.libros[titulo_modificar]["autor"] = autor
        self.libros[titulo_modificar]["año"] = año
        self.libros[titulo_modificar]["id"] = id
        self.libros[titulo_modificar]["descripcion"] = descripcion

        return(f"el libro '{titulo_modificar}' ha sido modificado exitosamente")

    def eliminar_libro(self):
        titulo_eliminar = input("ingrese el titulo del libro a eliminar: ").strip().lower()
        if titulo_eliminar in self.libros:
            del self.libros[titulo_eliminar]
            return(f"el libro '{titulo_eliminar}' ha sido eliminado exitosamente")
        else:
            return(f"Error: el libro '{titulo_eliminar}' no se escuentra en la biblioteca.")
        
    def mostrar_libro(self):
        titulo_mostrar = input("ingrese el titulo del libro a mostrar: ").strip().lower()
        if titulo_mostrar in self.libros:
            libro = self.libros[titulo_mostrar]
            return(f"los datos del libro '{titulo_mostrar}' son: Autor: {libro["autor"]}\n Año: {libro["año"]}\n ID: {libro["id"]}\n Descripcion: {libro["descripcion"]}")
        else:
            return(f"Error: el libro no se escuentra en la biblioteca.")

    def listar_libros(self):
        if self.libros:
            for titulo, datos in self.libros.items():
                return(f"{titulo}: {datos}")
        else:
            return("No hay libros registrados en la biblioteca.") 

mi_biblioteca = biblioteca()
mi_biblioteca.cargar_libros()

def menu():
    while True:
      

      print("\n--- Menu de la Biblioteca ---\n")
      print("1. Agregar libro")
      print("2. Modificar libro")
      print("3. Eliminar libro")
      print("4. Mostrar libro")
      print("5. Listar libros")
      print("6. Guardar y salir")

      opcion = int(input("ingrese una opcion: "))

      if opcion == 1:
          print(mi_biblioteca.agg_libro())
      elif opcion == 2:
          print(mi_biblioteca.modificar_libro())
      elif opcion == 3:
          print(mi_biblioteca.eliminar_libro()) 
      elif opcion == 4:
          print(mi_biblioteca.mostrar_libro())
      elif opcion == 5:
          print(mi_biblioteca.listar_libros())
      elif opcion == 6:
          print(mi_biblioteca.guardar_salir()) 
          break


menu()