import time
def constante(n):
    gaus = (n / 2) * (n + 1)
    return gaus

def run():
    n = 100
    
    tiempo_inicial = time.time()
    
    suma = constante(n)
    print('La suma es: ' + str(suma))

    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print('Tiempo: ' + str(tiempo_total))

if __name__ == "__main__":
    run()
