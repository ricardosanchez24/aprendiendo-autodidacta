'''
class libro:
    def __init__(self,titulo, autor, descripcion, año, id):
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.año = año
        self.id = id

    def mostrar_info(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nDescripción: {self.descripcion}\nAño: {self.año}\nID: {self.id}"

class usuario(libro):
    def __init__(self, nombre, id_usuario):
        super().__init__(titulo=None, autor=None, descripcion=None, año=None, id=None)
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append({
            "libro": libro,
            "fecha_prestamo": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def devolver_libro(self, titulo_libro):
        for prestamo in self.libros_prestados:
            if prestamo["libro"].titulo == titulo_libro:
                self.libros_prestados.remove(prestamo)
                return f"El libro '{titulo_libro}' ha sido devuelto."
        return f"El libro '{titulo_libro}' no está prestado por este usuario."

    def mostrar_libro(self):
        if not self.libros_prestados:
            return "No hay libros prestados."
        info_libros = []
        for prestamo in self.libros_prestados:
            libro_info = prestamo["libro"].mostrar_info()
            fecha_prestamo = prestamo["fecha_prestamo"]
            info_libros.append(f"{libro_info}\nFecha de Préstamo: {fecha_prestamo}\n")
        return "\n".join(info_libros)

class biblioteca(libro, usuario):
    def __init__(self):
        self.libros = {}

    def guardar_datos(self, archivo_json):
        with open(archivo_json, 'w') as archivo:
            json.dump(self.libros, archivo)

    def cargar_datos(self, archivo_json):
        try:
            with open(archivo_json, 'r') as archivo:
                self.libros = json.load(archivo)
        except FileNotFoundError:
            self.libros = {}

    def agregar_libro(self, libro):
        if libro.titulo in self.libros:
            return f"El libro '{libro.titulo}' ya existe en la biblioteca."
        self.libros[libro.titulo] = {
            "autor": libro.autor,
            "descripcion": libro.descripcion,
            "año": libro.año,
            "id": libro.id
        }
        return f"El libro '{libro.titulo}' ha sido agregado exitosamente a la biblioteca."

    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            del self.libros[titulo]
            return f"El libro '{titulo}' ha sido eliminado exitosamente."
        else:
            return f"Error: el libro '{titulo}' no se encuentra en la biblioteca."

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        info_libros = []
        for titulo, detalles in self.libros.items():
            libro_info = f"Título: {titulo}\nAutor: {detalles['autor']}\nDescripción: {detalles['descripcion']}\nAño: {detalles['año']}\nID: {detalles['id']}\n"
            info_libros.append(libro_info)
        return "\n".join(info_libros)

    def mostrar_libro(self, titulo):
        if titulo in self.libros:
            detalles = self.libros[titulo]
            return f"Título: {titulo}\nAutor: {detalles['autor']}\nDescripción: {detalles['descripcion']}\nAño: {detalles['año']}\nID: {detalles['id']}"
        else:
            return f"El libro '{titulo}' no se encuentra en la biblioteca."

    def modificar_libro(self, titulo, nuevo_libro):
        if titulo not in self.libros:
            return f"Error: el libro '{titulo}' no se encuentra en la biblioteca."
        self.libros[titulo] = {
            "autor": nuevo_libro.autor,
            "descripcion": nuevo_libro.descripcion,
            "año": nuevo_libro.año,
            "id": nuevo_libro.id
        }
        return f"El libro '{titulo}' ha sido modificado exitosamente."

'''                            