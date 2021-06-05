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

def busqueda_binaria(lista, comienzo, final, objetivo):

    # print('Buscando: ' + str(objetivo) + ' entre ' + str(lista[comienzo]) + ' y ' + str(lista[final-1]))
    
    contador = 0
    
    if comienzo > final:
        print(''' Un ciclo: ''' + str(contador))
        return False 
    
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        contador += 1
        print(''' Un ciclo: ''' + str(contador))
        return True
      
        

    elif lista[medio] < objetivo:
        contador += 1
        print(''' Un ciclo: ''' + str(contador))
        return busqueda_binaria(lista, medio + 1, final, objetivo)
         

    elif lista[medio] > objetivo:
        contador += 1
        print(''' Un ciclo: ''' + str(contador))
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
        

if __name__ == "__main__":

    tamano_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

# Busqueda binaria
    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo) 
    # print(''' BUSQUEDA BINARIA''')
    # print('El elemento ' + str(objetivo) + ' esta ' + 'en la lista.' if encontrado else 'No esta' + ' en la lista.')

    encontrado = busqueda_lineal(lista, objetivo)   