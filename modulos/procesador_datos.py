def obtener_edad(edad):
        
        if not isinstance(edad, int):
            return("Error, ingrese una edad valida")
            
        if edad >= 18 and edad <= 100:
            return ("es mayor de edad")
        elif edad < 18 and edad > 0:
           return ("menor de edad")
        else:
            return("Edad invalida")        
        

perfil = {
     "nombre": "pedro",
    "ciudad": "caracas",
    "edad": 18
}



def resumen_perfil(perfil):
     nombre = perfil["nombre"]
     ciudad = perfil["ciudad"]
     edad = perfil["edad"]

     estado_edad = obtener_edad(edad)

     frase = (f"el usuario {nombre} tiene {edad} años viven en {ciudad} y es {estado_edad} ")

     return frase      

#edad_usuario = usuario["edad"]
#estado_usuario = obtener_edad(edad_usuario)
#print(estado_usuario)