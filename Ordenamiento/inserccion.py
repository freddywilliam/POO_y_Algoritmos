def inserccion(lista):

    n = len(lista)

    for i in range(1, n)
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor
    return lista

def run():
    lista = [1, 9 , 19, 4, 3, 6, 10, 3]
    print(inserccion(lista))
    ordenamiento = inserccion(lista)
    print(ordenamiento)

if __name__ == "__main__":
        run()





        
    # for i in range(1, len(lista)):
    #     valor = lista[i]
    #     posicion_actual = i

    #     print( str(posicion_actual) + ' ES '+ str(valor))

    #     while posicion_actual > 0 and lista[posicion_actual - 1] > valor:
    #         lista[posicion_actual] = lista[posicion_actual - 1]
    #         posicion_actual -= 1