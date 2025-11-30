import json
import datetime
import os

# --- CONSTANTES DE ARCHIVOS ---
ARCHIVO_LIBROS = 'libros.json'
ARCHIVO_USUARIOS = 'usuarios.json'
ARCHIVO_PRESTAMOS = 'prestamos.json'
# --- CONSTANTE DE MULTA ---
TARIFA_MULTA_DIARIA = 5  # $5 por día de retraso

class libro:
    """Gestiona la colección de libros de la biblioteca."""
    def __init__(self):
        self.listado_libros = {}

    def _obtener_input_entero(self, mensaje):
        """Función auxiliar para manejar la entrada de números enteros (con manejo de errores)."""
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("⚠️ Error: Ingrese un número entero válido (ID o Año).")

    def agg_libro(self):
        """Permite agregar un nuevo libro a la colección."""
        titulo = input("Ingrese el título del libro: ").strip().lower()
        
        if titulo in self.listado_libros:
            return f"Error: El libro '{titulo.title()}' ya existe en la biblioteca."

        autor = input("Ingrese el autor del libro: ").strip().lower()
        descripcion = input("Ingrese una descripción del libro: ").strip().lower()
        
        # Uso del manejo de errores para el año y el ID
        año = self._obtener_input_entero("Ingrese el año del libro: ")
        id_libro = self._obtener_input_entero("Ingrese el ID del libro: ")

        self.listado_libros[titulo] = {
            "descripcion": descripcion,
            "autor": autor,
            "año": año,
            "id": id_libro,
            "estado": "disponible"
        }
        return f"El libro '{titulo.title()}' ha sido agregado exitosamente."

    def mostrar_libros(self):
        """Muestra la información de todos los libros."""
        if not self.listado_libros:
            return "No hay libros en la biblioteca."
        
        info_libros = ["\n--- LISTADO COMPLETO DE LIBROS ---"]
        for titulo, detalles in self.listado_libros.items():
            libro_info = (
                f"Título: {titulo.title()}\n"
                f"Autor: {detalles['autor'].title()}\n"
                f"Descripción: {detalles['descripcion'].capitalize()}\n"
                f"Año: {detalles['año']}\n"
                f"ID: {detalles['id']}\n"
                f"Estado: {detalles['estado'].upper()}\n"
                f"-----------------------------------"
            )
            info_libros.append(libro_info) 

        return "\n".join(info_libros)

    def mostrar_libro(self):
        """Busca y muestra la información de un libro específico."""
        titulo = input("Ingrese el título del libro que quiere mostrar: ").strip().lower()

        if titulo in self.listado_libros:
            detalles = self.listado_libros[titulo]
            return (
                f"\n--- DETALLES DEL LIBRO ---\n"
                f"Título: {titulo.title()}\n"
                f"Autor: {detalles['autor'].title()}\n"
                f"Descripción: {detalles['descripcion'].capitalize()}\n"
                f"Año: {detalles['año']}\n"
                f"ID: {detalles['id']}\n"
                f"Estado: {detalles['estado'].upper()}"
            )
        else:
            return f"El libro '{titulo.title()}' no se encuentra en la biblioteca."

    def modificar_libro(self):
        """Permite modificar los detalles de un libro existente."""
        titulo_modificar = input("Ingrese el título del libro a modificar: ").strip().lower()
        
        if titulo_modificar not in self.listado_libros:
            return f"Error: El libro '{titulo_modificar.title()}' no se encuentra en la biblioteca."
        
        if self.listado_libros[titulo_modificar]["estado"] != "disponible":
            return f"Error: El libro '{titulo_modificar.title()}' está actualmente prestado y no puede modificarse."

        print(f"\n--- Modificando '{titulo_modificar.title()}' ---")
        
        nuevo_autor = input("Ingrese el nuevo autor del libro: ").strip().lower()
        nueva_descripcion = input("Ingrese la nueva descripción del libro: ").strip().lower()
        
        # Uso del manejo de errores para el año y el ID
        nuevo_año = self._obtener_input_entero("Ingrese el nuevo año del libro: ")
        nuevo_id = self._obtener_input_entero("Ingrese el nuevo ID del libro: ")

        self.listado_libros[titulo_modificar].update({
            "autor": nuevo_autor,
            "descripcion": nueva_descripcion,
            "año": nuevo_año,
            "id": nuevo_id
        })
        
        return f"El libro '{titulo_modificar.title()}' ha sido modificado exitosamente."

    def eliminar_libro(self):
        """Elimina un libro de la colección."""
        titulo_eliminar = input("Ingrese el título del libro a eliminar: ").strip().lower()
        
        if titulo_eliminar not in self.listado_libros:
            return f"Error: El libro '{titulo_eliminar.title()}' no se encuentra en la biblioteca."

        if self.listado_libros[titulo_eliminar]["estado"] != "disponible":
            return f"Error: No se puede eliminar el libro '{titulo_eliminar.title()}' porque está prestado."
            
        del self.listado_libros[titulo_eliminar]
        return f"El libro '{titulo_eliminar.title()}' ha sido eliminado exitosamente."


class usuario():
    """Gestiona el registro de usuarios del sistema."""
    def __init__(self, libro_obj):
        self.listado_usuarios = {}
        # Se guarda la referencia al objeto libro
        self.libro = libro_obj 

    def _obtener_input_entero(self, mensaje):
        """Función auxiliar para manejar la entrada de números enteros (con manejo de errores)."""
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("⚠️ Error: Ingrese un número entero válido (ID).")

    def agg_usuario(self):
        """Agrega un nuevo usuario al sistema."""
        nombre = input("Ingrese el nombre completo del usuario: ").strip().lower()
        
        if nombre in self.listado_usuarios:
            return f"Error: El usuario '{nombre.title()}' ya está registrado."

        # Uso del manejo de errores para el ID
        id_usuario = self._obtener_input_entero("Ingrese el ID del usuario: ")
        
        self.listado_usuarios[nombre] = {
            "id_usuario": id_usuario,
            "prestamos_activos": 0 
        }
        return f"El usuario '{nombre.title()}' ha sido agregado exitosamente al sistema."

    def mostras_usuarios(self):
        """Muestra la información de todos los usuarios registrados."""
        if not self.listado_usuarios:
            return "No hay usuarios registrados en el sistema."
        
        info_usuarios = ["\n--- LISTADO COMPLETO DE USUARIOS ---"]
        for nombre, detalles in self.listado_usuarios.items():
            usuario_info = (
                f"Nombre: {nombre.title()}\n"
                f"ID Usuario: {detalles['id_usuario']}\n"
                f"Préstamos Activos: {detalles.get('prestamos_activos', 0)}\n"
                f"-----------------------------------"
            )
            info_usuarios.append(usuario_info) 

        return "\n".join(info_usuarios)

    def mostrar_usuario(self):
        """Muestra la información de un usuario específico."""
        nombre = input("Ingrese el nombre del usuario a buscar: ").strip().lower()
        
        if nombre in self.listado_usuarios:
            detalles = self.listado_usuarios[nombre]
            return (
                f"\n--- DETALLES DEL USUARIO ---\n"
                f"Nombre: {nombre.title()}\n"
                f"ID Usuario: {detalles['id_usuario']}\n"
                f"Préstamos Activos: {detalles.get('prestamos_activos', 0)}"
            )
        else:
            return f"El usuario '{nombre.title()}' no se encuentra en el sistema."

    def eliminar_usuario(self):
        """Elimina un usuario del sistema."""
        nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ").strip().lower()
        
        if nombre_eliminar not in self.listado_usuarios:
            return f"Error: El usuario '{nombre_eliminar.title()}' no se encuentra en el sistema."
        
        if self.listado_usuarios[nombre_eliminar].get("prestamos_activos", 0) > 0:
            return f"Error: No se puede eliminar a '{nombre_eliminar.title()}' porque tiene préstamos activos."
            
        del self.listado_usuarios[nombre_eliminar]
        return f"El usuario '{nombre_eliminar.title()}' ha sido eliminado exitosamente."


class prestamo():
    """Gestiona las transacciones de préstamo y devolución."""
    def __init__(self, usuario_obj, libro_obj):
        self.usuario = usuario_obj # Instancia de usuario
        self.libro = libro_obj     # Instancia de libro
        self.libros_prestados = {}
        self.id_prestamo = 1 

    def realizar_prestamo(self):
        titulo_libro = input("Ingrese el título del libro a prestar: ").strip().lower()
        nombre_usuario = input("Ingrese el nombre del usuario a realizar el préstamo: ").strip().lower()

        # 1. Validación de Libro
        if titulo_libro not in self.libro.listado_libros: 
            return f"Error: El libro '{titulo_libro.title()}' no está registrado en la biblioteca."
        
        libro_detalles = self.libro.listado_libros[titulo_libro]

        if libro_detalles["estado"] != "disponible":
            return f"Error: El libro '{titulo_libro.title()}' no está disponible (estado: {libro_detalles['estado'].upper()})."
        
        # 2. Validación de Usuario
        if nombre_usuario not in self.usuario.listado_usuarios:
            return f"Error: El usuario '{nombre_usuario.title()}' no está registrado."
        
        # 3. Registrar Transacción
        fecha_prestamo = datetime.date.today()
        fecha_vencimiento = fecha_prestamo + datetime.timedelta(days=14)
        id_prestamo_actual = str(self.id_prestamo) 

        self.libros_prestados[id_prestamo_actual] = {
            "titulo_libro": titulo_libro,
            "nombre_usuario": nombre_usuario,
            "fecha_prestamo": str(fecha_prestamo), 
            "fecha_vencimiento": str(fecha_vencimiento),
            "estado": "ACTIVO",
            "multa": 0.0,
            "fecha_devolucion_real": None
        }
        self.id_prestamo += 1 

        # 4. Actualizar estados
        self.libro.listado_libros[titulo_libro]["estado"] = "prestado"
        self.usuario.listado_usuarios[nombre_usuario]["prestamos_activos"] += 1

        return (
            f"✅ Préstamo realizado exitosamente.\n"
            f"Libro: {titulo_libro.title()} a {nombre_usuario.title()}.\n"
            f"ID Préstamo: {id_prestamo_actual}. Fecha de Vencimiento: {fecha_vencimiento}."
        )
    
    def devolver_libro(self):
        """Registra la devolución de un libro y aplica multas si es necesario."""
        titulo_libro = input("Ingrese el título del libro a devolver: ").strip().lower()

        prestamo_encontrado = None
        id_prestamo = None
        nombre_usuario_prestado = None 

        # 1. Buscar el préstamo ACTIVO por el título del libro
        for p_id_str, p_detalles in self.libros_prestados.items():
            if (p_detalles["titulo_libro"] == titulo_libro and 
                p_detalles["estado"] == "ACTIVO"):
                
                prestamo_encontrado = p_detalles
                id_prestamo = p_id_str
                nombre_usuario_prestado = p_detalles["nombre_usuario"]
                break
        
        if not prestamo_encontrado:
            return f"Error: No se encontró un préstamo ACTIVO para el libro '{titulo_libro.title()}'."
            
        # 2. Calcular multa
        fecha_devolucion = datetime.date.today()
        # Convertir la fecha de vencimiento (guardada como string) de nuevo a objeto date
        fecha_vencimiento = datetime.datetime.strptime(prestamo_encontrado["fecha_vencimiento"], '%Y-%m-%d').date()

        dias_retraso = (fecha_devolucion - fecha_vencimiento).days
        multa = 0.0
        mensaje_multa = "Devolución a tiempo."
        
        if dias_retraso > 0:
            multa = dias_retraso * TARIFA_MULTA_DIARIA
            mensaje_multa = f"ATENCIÓN: Retraso de {dias_retraso} días. Multa aplicada: ${multa:.2f}"
            
        # 3. Actualizar el registro del préstamo a DEVUELTO
        self.libros_prestados[id_prestamo]["estado"] = "DEVUELTO"
        self.libros_prestados[id_prestamo]["fecha_devolucion_real"] = str(fecha_devolucion)
        self.libros_prestados[id_prestamo]["multa"] = multa

        # 4. Actualizar el estado del libro y los préstamos activos del usuario
        if titulo_libro in self.libro.listado_libros:
             self.libro.listado_libros[titulo_libro]["estado"] = "disponible"
        
        if nombre_usuario_prestado in self.usuario.listado_usuarios:
            if self.usuario.listado_usuarios[nombre_usuario_prestado].get("prestamos_activos", 0) > 0:
                self.usuario.listado_usuarios[nombre_usuario_prestado]["prestamos_activos"] -= 1

        return f"✅ Devolución del libro '{titulo_libro.title()}' registrada exitosamente. {mensaje_multa}"

    def mostrar_prestamos_activos(self):
        """Muestra una lista de todos los préstamos que tienen el estado 'ACTIVO'."""
        activos = []
        for p_id, p_detalles in self.libros_prestados.items():
            if p_detalles["estado"] == "ACTIVO":
                info = (f"ID Préstamo: {p_id} | Libro: {p_detalles['titulo_libro'].title()} | "
                        f"Usuario: {p_detalles['nombre_usuario'].title()} | Vence: {p_detalles['fecha_vencimiento']}")
                activos.append(info)
        
        if activos:
            return "\n".join(["\n--- PRÉSTAMOS ACTIVOS ---"] + activos)
        else:
            return "No hay préstamos activos en este momento."


# --- CLASE GESTORA BIBLIOTECA (Contenedora) ---
class Biblioteca:
    """Clase principal que inicializa y coordina todos los gestores."""
    def __init__(self):
        
        # 1. Inicialización de gestores (Ahora con constructores simplificados)
        self.gestion_libros = libro() 
        self.gestion_usuarios = usuario(self.gestion_libros) 
        self.gestion_prestamos = prestamo(self.gestion_usuarios, self.gestion_libros)

        # 2. Cargar datos
        self.cargar_datos()

    # --- Métodos de Menú/Funcionalidad de Libros ---
    def menu_libros(self):
        """Menú para las operaciones CRUD de Libros."""
        while True:
            print("\n--- GESTIÓN DE LIBROS ---")
            print("1. Agregar Libro")
            print("2. Mostrar Todos los Libros")
            print("3. Modificar Libro (por título)")
            print("4. Eliminar Libro")
            print("5. Mostrar Libro Específico")
            print("6. Volver al Menú Principal")
            
            opc = input("Ingrese una opción (1-6): ")
            
            if opc == '1':
                print(self.gestion_libros.agg_libro())
            elif opc == '2':
                print(self.gestion_libros.mostrar_libros())
            elif opc == '3':
                print(self.gestion_libros.modificar_libro()) 
            elif opc == '4':
                print(self.gestion_libros.eliminar_libro())
            elif opc == '5':
                print(self.gestion_libros.mostrar_libro()) 
            elif opc == '6':
                return
            else:
                print("❌ Opción no válida. Intente de nuevo.")

    # --- Métodos de Menú/Funcionalidad de Usuarios ---
    def menu_usuarios(self):
        """Menú para las operaciones CRUD de Usuarios."""
        while True:
            print("\n--- GESTIÓN DE USUARIOS ---")
            print("1. Agregar Usuario")
            print("2. Mostrar Todos los Usuarios")
            print("3. Eliminar Usuario")
            print("4. Mostrar Usuario Específico")
            print("5. Volver al Menú Principal")

            opc = input("Ingrese una opción (1-5): ")

            if opc == '1':
                print(self.gestion_usuarios.agg_usuario())
            elif opc == '2':
                print(self.gestion_usuarios.mostras_usuarios())
            elif opc == '3':
                print(self.gestion_usuarios.eliminar_usuario())
            elif opc == '4':
                print(self.gestion_usuarios.mostrar_usuario()) 
            elif opc == '5':
                return
            else:
                print("❌ Opción no válida. Intente de nuevo.")


    # --- Métodos de Menú/Funcionalidad de Préstamos ---
    def menu_prestamos(self):
        """Menú para las operaciones de Préstamo."""
        while True:
            print("\n--- GESTIÓN DE PRÉSTAMOS ---")
            print("1. Realizar Préstamo")
            print("2. Devolver Libro")
            print("3. Mostrar Préstamos Activos")
            print("4. Volver al Menú Principal")

            opc = input("Ingrese una opción (1-4): ")

            if opc == '1':
                print(self.gestion_prestamos.realizar_prestamo())
            elif opc == '2':
                print(self.gestion_prestamos.devolver_libro())
            elif opc == '3':
                print(self.gestion_prestamos.mostrar_prestamos_activos()) 
            elif opc == '4':
                return
            else:
                print("❌ Opción no válida. Intente de nuevo.")
    
    # --- Métodos de Persistencia (Guardar/Cargar) ---
    def cargar_datos(self):
        """Carga los datos de los archivos JSON al iniciar el programa."""
        
        # Cargar Libros
        if os.path.exists(ARCHIVO_LIBROS):
            try:
                with open(ARCHIVO_LIBROS, 'r') as f:
                    self.gestion_libros.listado_libros = json.load(f)
                print(f"✅ Libros cargados desde {ARCHIVO_LIBROS}")
            except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
                print(f"❌ Error al cargar libros. Se iniciará con lista vacía: {e}")

        # Cargar Usuarios
        if os.path.exists(ARCHIVO_USUARIOS):
            try:
                with open(ARCHIVO_USUARIOS, 'r') as f:
                    self.gestion_usuarios.listado_usuarios = json.load(f)
                print(f"✅ Usuarios cargados desde {ARCHIVO_USUARIOS}")
            except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
                print(f"❌ Error al cargar usuarios. Se iniciará con lista vacía: {e}")

        # Cargar Préstamos
        if os.path.exists(ARCHIVO_PRESTAMOS):
            try:
                with open(ARCHIVO_PRESTAMOS, 'r') as f:
                    data = json.load(f)
                    self.gestion_prestamos.libros_prestados = data.get("prestamos", {})
                    
                    id_sig = data.get("id_prestamo_siguiente")
                    if isinstance(id_sig, int) and id_sig > 0:
                         self.gestion_prestamos.id_prestamo = id_sig
                    else:
                         # Recalcular ID si no se pudo cargar
                         max_id = max([int(k) for k in self.gestion_prestamos.libros_prestados.keys()], default=0)
                         self.gestion_prestamos.id_prestamo = max_id + 1
                         
                print(f"✅ Préstamos cargados desde {ARCHIVO_PRESTAMOS}")
            except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
                print(f"❌ Error al cargar préstamos. Se iniciará con lista vacía: {e}")


    def guardar_datos(self):
        """Guarda todos los datos en archivos JSON."""
        
        # Guardar Libros
        try:
            with open(ARCHIVO_LIBROS, 'w') as f:
                json.dump(self.gestion_libros.listado_libros, f, indent=4)
            print(f"💾 Datos de libros guardados en {ARCHIVO_LIBROS}")
        except Exception as e:
            print(f"❌ Error al guardar libros: {e}")

        # Guardar Usuarios
        try:
            with open(ARCHIVO_USUARIOS, 'w') as f:
                json.dump(self.gestion_usuarios.listado_usuarios, f, indent=4)
            print(f"💾 Datos de usuarios guardados en {ARCHIVO_USUARIOS}")
        except Exception as e:
            print(f"❌ Error al guardar usuarios: {e}")

        # Guardar Préstamos y el ID siguiente
        datos_prestamos = {
            "id_prestamo_siguiente": self.gestion_prestamos.id_prestamo,
            "prestamos": self.gestion_prestamos.libros_prestados
        }
        try:
            with open(ARCHIVO_PRESTAMOS, 'w') as f:
                json.dump(datos_prestamos, f, indent=4)
            print(f"💾 Datos de préstamos guardados en {ARCHIVO_PRESTAMOS}")
        except Exception as e:
            print(f"❌ Error al guardar préstamos: {e}")

# --- LÓGICA DEL MENÚ PRINCIPAL EXTERNO (Ejecución) ---

def mostrar_menu_principal():
    """Muestra el menú principal y pide la opción al usuario, con manejo de errores."""
    print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
    print("1.  Gestión de Libros")
    print("2.  Gestión de Usuarios")
    print("3.  Gestión de Préstamos")
    print("4.  Salir del Sistema")
    print("------------------------------------------")
    
    while True:
        try:
            opcion = input("Ingrese una opción (1-4): ")
            return int(opcion)
        except ValueError:
            print("⚠️ Error: Ingrese un número válido (1, 2, 3 o 4).")


def ejecutar_menu_principal():
    """Bucle principal de la aplicación."""
    # Creamos una única instancia de la clase Biblioteca.
    app = Biblioteca()

    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == 1:
            app.menu_libros()
        elif opcion == 2:
            app.menu_usuarios()
        elif opcion == 3:
            app.menu_prestamos()
        elif opcion == 4:
            print("\n⏳ Guardando datos antes de salir...")
            app.guardar_datos()
            print("👋 Gracias por usar el Sistema de Gestión de Biblioteca. ¡Adiós!")
            break
        else:
            print("❌ Opción no válida. Ingrese un número entre 1 y 4.")

# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    ejecutar_menu_principal()