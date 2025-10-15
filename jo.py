#Ejercicio: Calculadora de Calificaciones de Estudiantes 🎓
#El objetivo es crear un sistema simple para procesar la calificación final de un estudiante basándose en sus puntajes y determinar si aprobó o reprobó.

def calcular_promedio(nota1,nota2,nota3):

    promedio_suma = nota1 + nota2 + nota3
    promedio = promedio_suma / 3
    
    return promedio

def estado(promedio):
    
    if promedio >= 70 and promedio <= 100:
        estado_alumno = "aprobado"
    elif promedio >= 1 and promedio <= 69:
        estado_alumno = "reprobado"
    else:
        estado_alumno = "invalido"
        print("el numero es invalido")    
    
    return promedio, estado_alumno
            

def mostrar_resultado(nombre, promedio, estado_alumno):

    print(f"el estudiante {nombre}")
    print(f"tiene una calificacion de {promedio:.2f}")

    if estado_alumno == "invalido":
        print("ERROR!!! el estado es invalido ")
    else:
        print(f"el estado del alumno es {estado_alumno}")


nombre_estudiante = "santa maria"
n1, n2, n3 = 70, 65, 100

promedio_maria = calcular_promedio(n1, n2, n3)

promedio_final, estado_final = estado(promedio_maria)

mostrar_resultado(nombre_estudiante, promedio_final, estado_final)