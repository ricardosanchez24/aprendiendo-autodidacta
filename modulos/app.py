import procesador_datos as pd

usuarios = []

usuario1 = {
    "nombre": "juan",
    "ciudad": "barcelona",
    "edad": 22
}
usuario2 = {
    "nombre": "maria",
    "ciudad": "los angeles",
    "edad": 25
}
usuario3 = {
    "nombre": "Ricardo",
    "ciudad": "new york",
    "edad": 21
}
usuario4 = {
    "nombre": "david",
    "ciudad": "seattle",
    "edad": 30
}
usuario5 = {
    "nombre": "miguel",
    "ciudad": "petare",
    "edad": 17
}
usuarios.append(usuario1)
usuarios.append(usuario2)
usuarios.append(usuario3)
usuarios.append(usuario4)
usuarios.append(usuario5)

for usuario in usuarios:
    resultado = pd.resumen_perfil(usuario)
    print(resultado)