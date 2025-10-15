#crear lista de tareas

from datetime import datetime

class Tarea:
    def __init__(self, titulo, prioridad="media"):
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha_creacion = datetime.now()
        self.completada = False
        self.fecha_finalizada = None
    
    def tarea_completada(self):
        self.fecha_finalizada = datetime.now()
        self.completada = True
        #if self.completada: (hacer la info)
        

    def obtener_informacion(self):
        return f"tarea: {self.titulo}, prioridad: {self.prioridad}, fecha de creacion: {self.fecha_creacion}, tarea completada: {self.completada}, fecha de completacion: {self.fecha_finalizada}"    


t1 = Tarea("comprar pan", "Alta")
t1.tarea_completada()

print(t1.obtener_informacion())