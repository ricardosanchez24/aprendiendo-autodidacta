## poo_ejemplo.py
# ==============================================================================
# EJEMPLO COMPLETO DE PROGRAMACIÓN ORIENTADA A OBJETOS (POO) EN PYTHON
# ==============================================================================

### 1. CLASE BASE: VEHICULO (Padre)
class Vehiculo:
    """
    Clase base que sirve como plantilla para todos los vehículos.
    Demuestra Clases, Atributos y Encapsulamiento.
    """
    
    # Constructor: Se llama al crear una nueva instancia (Objeto)
    def __init__(self, marca, modelo, color):
        # Atributos públicos
        self.marca = marca
        self.modelo = modelo
        
        # Atributo "privado" (Encapsulamiento): 
        # El doble guion bajo '__' sugiere que no debe accederse directamente.
        self.__color = color 
        
    # Método público para describir el vehículo
    def describir(self):
        """Retorna una descripción básica del vehículo."""
        return f"Este es un vehículo de la marca {self.marca}, modelo {self.modelo}."

    # Método para acceder de forma controlada al atributo "encapsulado"
    def obtener_color(self):
        """Método para obtener el color de forma segura."""
        return self.__color

# ------------------------------------------------------------------------------

### 2. CLASE HIJA: COCHE (Herencia)
class Coche(Vehiculo):
    """
    Clase hija que hereda de Vehiculo.
    Demuestra Herencia y Polimorfismo (al sobreescribir describir()).
    """
    
    def __init__(self, marca, modelo, color, num_puertas):
        # 1. HERENCIA: Llama al constructor del padre (Vehiculo) para 
        #    inicializar marca, modelo y color.
        super().__init__(marca, modelo, color) 
        
        # 2. Atributo propio de la clase Coche
        self.num_puertas = num_puertas

    # POLIMORFISMO: Sobreescribiendo el método 'describir' del padre (Vehiculo)
    def describir(self):
        """Retorna una descripción específica de Coche."""
        # Implementación propia para Coche, usando atributos heredados y propios.
        return f"Soy un {self.marca} {self.modelo} y tengo {self.num_puertas} puertas."

    # Método propio de la clase Coche
    def abrir_maletero(self):
        """Comportamiento único de los coches."""
        return "El maletero del coche está abierto."

# ------------------------------------------------------------------------------

### 3. CLASE INDEPENDIENTE: BICICLETA (Polimorfismo)
class Bicicleta:
    """
    Clase independiente que tiene el mismo método 'describir' que Coche y Vehiculo.
    Esencial para el ejemplo de Polimorfismo.
    """
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

    # Mismo nombre de método 'describir' con implementación propia
    def describir(self):
        """Retorna una descripción específica de Bicicleta."""
        return f"Soy una bicicleta de la marca {self.marca} de tipo {self.tipo}."

# ------------------------------------------------------------------------------

### 4. DEMOSTRACIÓN DEL CÓDIGO

if __name__ == "__main__":
    print("--- 🚗 DEMOSTRACIÓN DE POO ---")
    
    ## A) CLASE, INSTANCIAS Y ENCAPSULAMIENTO
    print("\n## A) CLASE, INSTANCIAS Y ENCAPSULAMIENTO:")
    
    # Crear dos instancias (Objetos) de la clase Vehiculo
    mi_coche_base = Vehiculo("Toyota", "Corolla", "Rojo")
    mi_camioneta = Vehiculo("Ford", "Raptor", "Negro")
    
    # Usar métodos y atributos
    print(mi_coche_base.describir())
    # Acceso controlado al atributo encapsulado
    print(f"El color es: {mi_coche_base.obtener_color()}") 

    # ---
    
    ## B) HERENCIA
    print("\n## B) HERENCIA:")
    
    # Crear una instancia de la clase hija Coche
    mi_deportivo = Coche("Ferrari", "488", "Amarillo", 2)
    
    # Usamos métodos heredados del padre (Vehiculo)
    print(f"Descripción heredada: {mi_deportivo.obtener_color()}") 
    
    # Usamos el método propio del hijo (Coche)
    print(f"Comportamiento propio: {mi_deportivo.abrir_maletero()}")

    # ---
    
    ## C) POLIMORFISMO
    print("\n## C) POLIMORFISMO:")

    # Lista que contiene instancias de diferentes clases (Coche y Bicicleta)
    lista_de_cosas = [
        mi_deportivo,                       # Instancia de Coche
        Bicicleta("Trek", "Montaña"),       # Instancia de Bicicleta
        Vehiculo("Avión", "Boeing", "Blanco") # Instancia de Vehiculo
    ]

    for item in lista_de_cosas:
        # Llamamos al mismo método 'describir()' en todos los objetos.
        # El resultado es diferente porque cada clase tiene su propia implementación.
        print(f" -> {item.describir()}") 

    # Output del Polimorfismo:
    #  -> Soy un Ferrari 488 y tengo 2 puertas. (Desde Coche)
    #  -> Soy una bicicleta de la marca Trek de tipo Montaña. (Desde Bicicleta)
    #  -> Este es un vehículo de la marca Avión, modelo Boeing. (Desde Vehiculo)