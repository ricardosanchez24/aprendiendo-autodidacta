#crear calculadora de edad
import datetime
import math
def calcular_edad(año,mes,dia): 
    fecha_hoy = datetime.date.today()
    
    fecha_nacimiento = datetime.date(año,mes,dia)

    diferencia_dias = fecha_hoy - fecha_nacimiento

    dias_totales = diferencia_dias.days

    año_calculado = dias_totales / 365.25
    
    edad_entera = int(math.floor(año_calculado))

    if fecha_hoy.month >= fecha_nacimiento.month:
        mes_calculado = fecha_hoy.month - fecha_nacimiento.month

    elif fecha_hoy.month < fecha_nacimiento.month:
        mes_calculado = fecha_hoy.month - fecha_nacimiento.month + 12

    if fecha_hoy.day >= fecha_nacimiento.day:
        dia_calculado = fecha_hoy.day - fecha_nacimiento.day
    else:
        # Tomar prestado un mes
        if mes_calculado == 0:
            mes_calculado = 11
            edad_entera -= 1
        else:
            mes_calculado -= 1
        mes_anterior = fecha_hoy.month - 1 if fecha_hoy.month > 1 else 12

        año_anterior = fecha_hoy.year if fecha_hoy.month > 1 else fecha_hoy.year - 1

        dias_ultimo_mes = (datetime.date(año_anterior, mes_anterior, 1) - datetime.timedelta(days=1)).day
        
        dia_calculado = dias_ultimo_mes - fecha_nacimiento.day + fecha_hoy.day


    print(f"su edad es de: {edad_entera} años, {mes_calculado} meses, {dia_calculado} dias")
try:
    tu_año = int(input("ingrese su año de nacimiento: "))
    tu_mes = int(input("ingrese su mes de nacimiento: "))
    tu_dia = int(input("ingrese su dia de nacimiento: "))
except:
    print("Solo puede ingresar numeros")
calcular_edad(tu_año,tu_mes,tu_dia)    