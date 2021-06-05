# SUma lineal y constante mas tiempos 
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
            

def suma_constante(n):
    
    gaus = (n // 2) * (n + 1)
    return gaus
      
def run():

    n = int(input('Valor: '))
    opcion = int(input('Opcion: '))

    tiempo_uno = time.time()

    total = suma_lineal(n)
    print(total)

    tiempo_dos = time.time()

    total_constante = suma_constante(n)
    print(total_constante)

    tiempo_tres =time.time()

    tiempo_lineal = round(tiempo_dos - tiempo_uno, 5)
    tiempo_constante = round(tiempo_tres - tiempo_dos, 100)

    if opcion == 1:
        print('Tiempo Lineal: ' + str(tiempo_lineal))
    elif opcion == 2:
        print('Tiempo Constante: ' + str(tiempo_constante))

    

    
    

       
if __name__ == "__main__":
    run()