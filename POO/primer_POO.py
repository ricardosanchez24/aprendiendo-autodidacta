class producto:

    def __init__(self,nombre, precio, stock=0, descuento=False):
        self.nombre_producto = nombre
        self.precio_producto = precio
        self.stock_producto = stock
        self.descuento = descuento

    def aplicar_descuento(self, porcentaje):
        
        self.precio_producto = self.precio_producto - (self.precio_producto * porcentaje)
        self.descuento = True

    def obtener_info(self):
        return (f"producto: nombre: {self.nombre_producto}, precio: {self.precio_producto}, stock: {self.stock_producto}.")        

producto1 = producto("leche", 12.99,)
producto2 = producto("galletas", 7.99, 100, True)
producto3 = producto("Zumo de Naranja", 5.00)

print(f"el producto {producto3.nombre_producto} tiene un precio inicial de {producto3.precio_producto}")
producto3.aplicar_descuento(0.20) 
print(f"producto con descuento: {producto3.precio_producto}\n")

print(producto2.obtener_info())

       

