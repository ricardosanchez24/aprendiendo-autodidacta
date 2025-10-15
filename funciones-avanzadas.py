def saludar_usuario(nombre,saludo="hola",idioma="es"):
    return (f"{saludo},{nombre}. Bienvenido") # return se utiliza para que retorne algun o algunos valores y puedan ser usados en otra parte del codigo ejem: una variable con un nombre puede utilizarse en otra funcion gracias al return

llamada1 = saludar_usuario("alex")    

llamada2 = saludar_usuario("juan","que gusto conocerte")

llamada3 = saludar_usuario("maria",idioma="en")

llamada4 = saludar_usuario("juan","bonjour","fr")

print(llamada1) # gracias al return se puede almacenar la funcion en una variable para llamarla