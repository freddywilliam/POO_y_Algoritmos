# Tiempo y suma lineal 
import time
def suma_lineal(n):
    
    total_lineal = 0
    inicio = 0

    while inicio <= n:
        total_lineal += inicio
        inicio += 1
        if inicio == n + 1:
            total_lineal
    return total_lineal
            
def run():
   

    n = 100
    

    tiempo_inicial = time.time()

    total = suma_lineal(n)
    print(total)

    tiempo_final = time.time()

    tiempo_total = round(tiempo_final - tiempo_inicial, 10)
    print('Tiempo: ' + str(tiempo_total))

if __name__ == "__main__":
    run()