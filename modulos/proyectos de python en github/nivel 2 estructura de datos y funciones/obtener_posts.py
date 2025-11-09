import requests
import json

# URL del recurso al que queremos acceder (una lista de post)
URL_API = "https://jsonplaceholder.typicode.com/posts"

print(f"Haciendo solicitud GET a: {URL_API}")

try:
    # 1. Realizar la solicitud GET
    # La función requests.get() devuelve un objeto 'Response'.
    respuesta = requests.get(URL_API, verify=False)

    # 2. Verificar el código de estado HTTP
    # El código 200 significa "OK" (Solicitud exitosa).
    if respuesta.status_code == 200:
        print("✅ Solicitud exitosa (Código de estado 200)")

        # 3. Acceder a los datos JSON
        # El método .json() parsea el texto de la respuesta y lo convierte en una lista o diccionario de Python.
        datos_json = respuesta.json()

        # 4. Procesar y mostrar la información
        # Mostramos cuántos posts obtuvimos y el título del primer post.
        print(f"\nNúmero total de posts recibidos: {len(datos_json)}")

        # Accedemos al primer elemento de la lista (que es un diccionario)
        primer_post = datos_json[0]

        print("--- Detalles del Primer Post ---")
        print(f"ID del Usuario: {primer_post['userId']}")
        print(f"ID del Post: {primer_post['id']}")
        print(f"Título: **{primer_post['title']}**")
        print(f"Cuerpo: {primer_post['body'][:50]}...") # Mostramos solo 50 caracteres del cuerpo
        print("------------------------------")

    else:
        # Manejo de errores si la API devuelve otro código (404, 500, etc.)
        print(f"❌ Error al hacer la solicitud. Código de estado: {respuesta.status_code}")
        print(f"Mensaje de error: {respuesta.text}")

except requests.exceptions.RequestException as e:
    # Manejo de errores de conexión (ej. no hay internet, DNS falla)
    print(f"❌ Error de conexión: {e}")