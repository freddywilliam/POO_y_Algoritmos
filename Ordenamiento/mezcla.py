import random

def mezcla(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(str(izquierda) + '*' *5 + str(derecha))

        # Llamada recursiva
        mezcla(izquierda)
        mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0

        # Iterador para lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            print('''      
            
                    EMPIEZA CICLO
            
                 ''')

            print(str(izquierda) + '*' *5 + str(derecha))
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
                print('izq < derecha = agrego izq a lista principal: ' + str(lista))
                
            else:
                lista[k] = derecha[j]
                j += 1
                print('izq > derecha = agrego derecha a lista principal: ' + str(lista))
                
            print('La lista principal ahora me queda asi: ' + str(lista))
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            print('La lista izquierda es: ')
            print(izquierda)
            print('Ordeno')
            
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1  
            print('La lista derecha es: ')
            print(derecha)
            print('Ordeno')
            
        print('La lista final es: ')
        print(lista)
        print('=' * 50)
    return lista

if __name__ == "__main__":

    tamano_lista = int(input('De que tamano sera la lista? '))
   
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    print('-' * 20)

    lista_ordenada = mezcla(lista) 
    print(lista_ordenada)