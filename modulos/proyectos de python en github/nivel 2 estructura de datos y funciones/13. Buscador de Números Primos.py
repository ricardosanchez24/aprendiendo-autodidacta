import time
total_numero = []
tiempo_inicial = time.time()

def generar_primo():
    print("rango del 1 al 100")
    for i in range(2,101):
        total_numero.append(i)
               
    return  total_numero   
    
    
def verificar_primo(total_numero):
    contador_primo = 0
    
    for i in total_numero:
        es_primo = True
        for j in range(2,i):
           if i % j == 0:
               es_primo = False
               break
        if es_primo == True:
            contador_primo += 1
           
    return contador_primo           

numero = generar_primo()

prueba = verificar_primo(numero);
print(f"numeros primos encontrados: {prueba}")

tiempo_final = time.time()
duracion_final = tiempo_final - tiempo_inicial
print(f"el tiempo de ejcucion fue de: {duracion_final:.4f} segundos")    