perfil_usuario = {
    "nombre" : "alejandro",
    "edad" : 18,
    "ciudad" : "new york",
    "intereses" : ["jugar al futbol", "ver peliculas", "leer libros"]
}

print(perfil_usuario["edad"])
print(perfil_usuario["intereses"] [1] ) #acceder al segundo valor de una lista dentro de un diccionario

perfil_usuario["ciudad"] = "barcelona" # modificar un valor

perfil_usuario["email"] = "correo@correo.com" # agg una clave y valor nuevos

del perfil_usuario["edad"] # eliminar una clave y su valor

print(perfil_usuario)


base_de_datos = []

usuario1 = {"nombre":"marcos","edad": 35, "ciudad" : "new york","intereses" : ["jugar al futbol", "ver peliculas", "leer libros"]}
usuario2 = {"nombre":"javier","edad": 25, "ciudad" : "barcelona","intereses" : ["correr motos", "ver comedia", "arreglar motos"]}
usuario3 = {"nombre":"juan","edad": 22, "ciudad" : "maracaibo","intereses" : ["jugar al futbol", "ver beisbol", "entrenar en el gym"]}

base_de_datos.append(usuario1)
base_de_datos.append(usuario2)
base_de_datos.append(usuario3)

for diccionario in base_de_datos:
    print(f"el usuario {diccionario["nombre"]} vive en {diccionario["ciudad"]}") #con el {diccionario[clave]} accedemos a los valores de cada diccionario dentro de la lista