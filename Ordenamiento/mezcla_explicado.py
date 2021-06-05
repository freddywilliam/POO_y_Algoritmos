import random

def mezcla(lista):
    print( '-' * 10 + 'DIVIDO' + '-' * 10  )
    if len(lista) > 1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(str(izquierda) + '*' *5 + str(derecha))

        # Llamada recursiva
        mezcla(izquierda)
        mezcla(derecha)

        print( '-' * 10 + 'CREO CONTADORES' + '-' * 10  )

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0

        # Iterador para lista principal
        k = 0

        print('izquierda: ' + str(i))
        print('derecha: ' + str(j))
        print('principal: ' + str(k))

        print( '-' * 10 + 'COMPARO LAS SUBLISTAS' + '-' * 10  )
        # print('izquierda < derecha = lista principal = izquierda')
        # print('izquierda > derecha = lista principal = derecha')
        # print('Se agrega el menor primero')
        # print('Se repite hasta obtener dos mitades ordenadas')
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
                print('izquierda: ' + str(lista))
            else:
                lista[k] = derecha[j]
                j += 1
                print('derecha: ' + str(lista))
            k += 1
        
        print( '-' * 10 + 'AGREGO A LISTA PRINCIPAL' + '-' * 10  )
        print('')
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j< len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print('Izquierda: ' + str(izquierda) + 'Derecha: '  + str(derecha))
    return lista

if __name__ == "__main__":

    tamano_lista = int(input('De que tamano sera la lista? '))
   
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print('Lista principal: ' +str(lista))
    print('-' * 20)

    lista_ordenada = mezcla(lista) 
    
    
    print(lista_ordenada)