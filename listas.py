lista_compras = ["pan", "leche", "huevos"]

print(lista_compras)

lista_compras.append("jamon")
print(lista_compras)

lista_compras.remove("leche")
print(lista_compras)

lista_compras.insert(0,"jugo de manzana")#insert se utiliza para agg en una posicion especifica deseada
print(lista_compras)

for indice, compra in enumerate (lista_compras, start=1):
    print(f"{indice}: {compra}")