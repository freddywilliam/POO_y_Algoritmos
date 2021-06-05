import time
import sys

def factorial(n):
    respuesta = 1
    
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == "__main__":
   
    sys.setrecursionlimit(1000000000)
    n = 10000000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print('Tiempo iterativa: ' + str(final - comienzo))

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print('Tiempo recursiva: ' + str(final - comienzo))

   