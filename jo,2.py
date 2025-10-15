#codigo corregido por la IA

# --- Tarea 1: Funciones de Cálculo ---

def calcular_promedio(nota1, nota2, nota3):
    """Calcula y retorna el promedio de tres notas."""
    promedio_suma = nota1 + nota2 + nota3
    promedio = promedio_suma / 3
    # NOTA: Python maneja el tipo flotante automáticamente
    return promedio

def determinar_estado(promedio):
    """Determina y retorna el estado del estudiante basado en el promedio."""
    
    # 1. Validación de número (se asume un rango 0 a 100)
    if promedio < 0 or promedio > 100:
        return "Inválido" # Retorna la cadena "Inválido" para ser manejada

    # 2. Lógica de aprobación (más simple porque ya sabemos que el promedio es válido)
    if promedio >= 70:
        estado_alumno = "Aprobado"
    else: # Si no es >= 70, y es válido, debe ser Reprobado
        estado_alumno = "Reprobado"
        
    return estado_alumno

def mostrar_resultados(nombre, promedio, estado):
    """Imprime el resumen de los resultados. NO retorna nada."""
    print("\n" + "="*40)
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}") # Formateo para dos decimales
    
    if estado == "Inválido":
        print("¡ERROR! El promedio es Inválido (fuera de rango 0-100).")
    else:
        print(f"Estado Final: {estado}")
    print("="*40)


# --- Tarea 2: Flujo Principal ---

# 1. Datos del estudiante
nombre_estudiante = "Santa María"
n1, n2, n3 = 75, 88, 62 

# 2. Flujo de llamadas
# Llama a calcular_promedio y GUARDA su retorno
promedio_final = calcular_promedio(n1, n2, n3)

# Llama a determinar_estado usando el promedio_final
estado_final = determinar_estado(promedio_final)

# Llama a mostrar_resultados con todos los datos procesados
mostrar_resultados(nombre_estudiante, promedio_final, estado_final)

# --- Ejemplo de otro estudiante (fácil de reusar) ---
nombre_ejemplo = "Juan Pérez"
p1, p2, p3 = 100, 95, 98

promedio_juan = calcular_promedio(p1, p2, p3)
estado_juan = determinar_estado(promedio_juan)
mostrar_resultados(nombre_ejemplo, promedio_juan, estado_juan)