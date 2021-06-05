import random

def busqueda_lineal(lista, objetivo):
    match = False
    contador_lineal = 0
    # O(n) Busqueda Lineal
    for elemento in lista:  
        contador_lineal += 1
        if elemento == objetivo:
            contador_lineal += 1
            match = True
            break
        
    print('Iteraciones: ' + str(contador_lineal))
    
    return match
   

if __name__ == "__main__":

    tamano_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)    
    
    print('El elemento ' + str(objetivo) + ' esta ' + 'en la lista.' if encontrado else 'No esta' + ' en la lista.')
