import requests
import json
import sys
#obtiene las tasas de cambio desde una API
def obtener_tasa():
    #URL de la API para obtener tasas de cambio
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:
       #envia una solicitud de informacion con GET a la API
       respuesta = requests.get(url,timeout=10)#tiempo de espera de 10 segundos

       respuesta.raise_for_status()#verifica si la solicitus fue exitosa

       #convierte la respuesta JSON en un diccionario de python
       datos = respuesta.json()

       #retorna las tasas de cambio 
       return datos["rates"]
    #manejo del tiempo de espera
    except requests.exceptions.Timeout:
        #print("Error: la solicitud excedio el tiempo de espera")
        return None
    #manejo de errores de conexion y repuesta de la API (codigos 4xx y 5xx)
    except requests.exceptions.RequestException as e:
        #print(f"Error: no se pudieron obtener las tasas de cambio. detalle: {e}")
        return None
    #manejo de error si no se puede codificar JSON
    except json.JSONDecodeError:
       #print("Error: no se pudo procesar la respuesta de la API (JSON invalido)")
       return None


#convierte una cantidad de una moneda a otra usando las tasas de cambio
def convertir_moneda(cantidad,moneda_origen, moneda_cambio,tasa_cambio):
    if moneda_cambio not in tasa_cambio:
        print("Error: Moneda no soportada, ingrese el codigo de moneda valido(USD,EUR,etc)")
        return None
    #convierte la cantidad a USD si la moneda de origen no es USD
    if moneda_origen != "USD":
      #verifica si la moneda de origen esta en las tasas de cambio
        if moneda_origen not in tasa_cambio:
           print("Error: Moneda no soportada, ingrese el codigo de la moneda(USD,EUR,etc)")
           return None
      #convertimos a dolares
        cantidad_usd = cantidad / tasa_cambio[moneda_origen]
     
      #convertirla a la moneda de cambio deseada
        return cantidad_usd * tasa_cambio[moneda_cambio]
     
     #si es USD, simplemente usamos la cantidad original
    else:
      return cantidad * tasa_cambio[moneda_cambio]   
    
#ejemplo de uso

# 1. Obtener las tasas de cambio
tasas = obtener_tasa() 
if tasas is None:
    # Si obtener_tasa falló, salimos del programa inmediatamente
    sys.exit(1)

# 2. Pedir al usuario la cantidad y manejar errores de entrada (ValueError)
try:
    # 💥 Cambio clave: Usar float() para permitir decimales en la cantidad
    cantidad_cambiar = float(input("Ingrese la cantidad a cambiar: "))
except ValueError:
    print("❌ Error: Debe ingresar un valor numérico válido para la cantidad.")
    sys.exit(1) 

# 3. Pedir al usuario las monedas
# Se añade un print informativo antes para que el usuario sepa qué ingresar
print("\nℹ️ Códigos disponibles (ejemplo): USD, EUR, ARS, JPY, GBP...")
moneda_origen = input("Ingrese la moneda de origen: ").strip().upper() # .strip() limpia espacios
moneda_cambio = input("Ingrese la moneda de cambio: ").strip().upper() # .strip() limpia espacios

# 4. Realizar la conversión
resultado = convertir_moneda(cantidad_cambiar, moneda_origen, moneda_cambio, tasas) 

# 5. Imprimir el resultado
if resultado is not None:
    print("\n" + "="*50)
    print(f"✅ Conversión exitosa:")
    # 💥 Cambio clave: Formato de salida con dos decimales y separador de miles (opcional)
    print(f"Se cambió {cantidad_cambiar:,.2f} {moneda_origen} a {resultado:,.2f} {moneda_cambio}")
    print("="*50)
else:
    # Este mensaje se muestra si convertir_moneda retornó None
    print("\n⚠️ La conversión no pudo completarse. Verifique los códigos de moneda ingresados.")