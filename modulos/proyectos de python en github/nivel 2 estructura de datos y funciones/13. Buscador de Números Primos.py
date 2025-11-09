import time
total_numero = []

'''
def generar_primo():
    print("rango del 1 al 100")
    for i in range(2,numeros_grandes):
        total_numero.append(i)
               
    return  total_numero   
'''    
def es_primo(n):
    primo = [True] * (n + 1)
    primo[0] = primo[1] = False

    selector = 2

    while selector * selector <= n:

        if primo[selector]:
            for i in range(selector*selector,n+1,selector):
                primo[i] = False

        selector += 1

    v = [x for x,primo in enumerate(primo) if primo]
    return v

prueba = es_primo(10000)
print(prueba)
''' 
def verificar_primo(total_numero):
    contador_primo = 0 # 1
    
    for i in total_numero: # n
        es_primo = True#n
        for j in range(2,i):#n´2
           if i % j == 0:#n´2
               es_primo = False#n´2
               break#n´2
        if es_primo == True: #n
            contador_primo += 1#n
          
    return contador_primo # 1          
  
numero = generar_primo()
tiempo_inicial = time.time()

prueba = verificar_primo(numero);
print(f"numeros primos encontrados: {prueba}")

tiempo_final = time.time()
duracion_final = tiempo_final - tiempo_inicial
print(f"el tiempo de ejcucion fue de: {duracion_final:.4f} segundos")    
'''