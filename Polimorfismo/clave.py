import random
def run():
    
    minusculas = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    mayusculas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    numeros = ('1', '2', '3', '4', '5', '6', '7', '8')
    signos = ('*', '&', '^', '%', '$', '#', '@', '!')
    clave = []
    
    for i in range(0, 2):
        
        aleatorio = random.randint(0, 7)
        clave.append(numeros[aleatorio])

        aleatorio = random.randint(0, 7)
        clave.append(mayusculas[aleatorio])

        aleatorio = random.randint(0, 7)
        clave.append(signos[aleatorio])
        
        aleatorio = random.randint(0, 7)
        clave.append(minusculas[aleatorio])

    clave = ''.join(clave)
    print('Esta es tu clave: ' + clave)
        

if __name__ == '__main__':
    run()


