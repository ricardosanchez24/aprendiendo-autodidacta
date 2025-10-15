#Descripción Cualitativa: Debes crear un programa que funcione como un conversor de temperatura práctico, donde el usuario pueda:
#Elegir entre convertir de Celsius a Fahrenheit o viceversa
#Ingresar la temperatura a convertir
#Ver el resultado formateado con el símbolo de grados
#Convertir múltiples temperaturas sin reiniciar el programa
#Ver una tabla de conversiones comunes El programa debe ser útil para situaciones cotidianas como #verificar el clima o cocinar.

#def celsius_f(temperatura):
#    conversion = (temperatura * 9/5) + 32
#    print(f"{temperatura}°C = {conversion:.2f}°F")


#def Fahrenheit_c(temperatura):
#    conversion = (temperatura - 32) * 5/9
#    print(f"{temperatura}°F = {conversion:.2f}°C")
  

#while True:
#    temperatura = int(input("ingrese la temperatura a convertir: "))
 #   unidad_temperatura = input("ingrese la unidad de temperatura a convertir en minisculas(C/F): ")
#
#    if unidad_temperatura == "c":
 #       celsius_f(temperatura)
 #   elif unidad_temperatura == "f":
 #       Fahrenheit_c(temperatura)
 #   else:
 #       print("Error, solo puede ingresar c o f")

 #   salida = input("¿seguir con el programa?(s/n):")
 #   if salida == "s":
 #       print("siguiendo el programa")
 #   elif salida == "n":
 #       print("Programa finalizado")
 #       break
  #  else:
  #      print("ingrese solo 's' o 'n' ")    
#codigo mejorado
def celsius_a_fahrenheit(temperatura):
    """
    Convierte una temperatura de Celsius (°C) a Fahrenheit (°F).

    Args:
        temperatura (float): La temperatura en grados Celsius.
    
    Returns:
        float: La temperatura convertida a grados Fahrenheit.
    """
    # Fórmula de conversión: (C * 9/5) + 32
    conversion = (temperatura * 9/5) + 32
    print(f"{temperatura:.2f}°C = {conversion:.2f}°F")
    return conversion


def fahrenheit_a_celsius(temperatura):
    """
    Convierte una temperatura de Fahrenheit (°F) a Celsius (°C).

    Args:
        temperatura (float): La temperatura en grados Fahrenheit.
    
    Returns:
        float: La temperatura convertida a grados Celsius.
    """
    # Fórmula de conversión: (F - 32) * 5/9
    conversion = (temperatura - 32) * 5/9
    print(f"{temperatura:.2f}°F = {conversion:.2f}°C")
    return conversion
 

# --- Programa Principal ---

while True:
    try:
        # Usamos float() para permitir temperaturas con decimales (más preciso)
        temperatura = float(input("Ingrese la temperatura a convertir: "))
    except ValueError:
        # Manejo de error si la entrada no es un número
        print("❌ Error: Por favor, ingrese un valor numérico válido para la temperatura.")
        continue # Vuelve al inicio del bucle

    # Se convierte la entrada a mayúsculas para un manejo más flexible (el usuario puede escribir 'c' o 'C')
    unidad_temperatura = input("Ingrese la unidad de temperatura a convertir (C/F): ").strip().upper()

    if unidad_temperatura == "C":
        # Llama a la función de Celsius a Fahrenheit
        celsius_a_fahrenheit(temperatura)
    elif unidad_temperatura == "F":
        # Llama a la función de Fahrenheit a Celsius
        fahrenheit_a_celsius(temperatura)
    else:
        print("⚠️ Error: Solo puede ingresar 'C' (Celsius) o 'F' (Fahrenheit).")
        # Continúa para no preguntar si quiere salir inmediatamente después de un error de unidad
        continue 

    # Preguntar si desea continuar
    salida = input("¿Desea realizar otra conversión? (S/N): ").strip().upper()
    
    if salida == "S":
        print("➡️ Reiniciando el programa para una nueva conversión...")
        # No se necesita 'continue', el bucle 'while True' se reinicia automáticamente
    elif salida == "N":
        print("✅ Programa finalizado. ¡Gracias!")
        break # Sale del bucle y termina el programa
    else:
        # En caso de una entrada inválida para continuar/salir
        print("❌ Entrada no válida. Por favor, ingrese solo 'S' para continuar o 'N' para finalizar.")
        # Se podría optar por finalizar el programa aquí o volver a preguntar, pero para simplificar, continuamos.
        
# Fin del script
          