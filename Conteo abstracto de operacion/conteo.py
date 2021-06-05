
def f(x):
    respuesta = 0

    print(''' EMPIEZA PRIMER LOOP ''')

    for i in range(10):
        respuesta  += 1
        print('Va de uno en uno: ' + str(respuesta))
        print('Se suma de uno en uno: ' + str(respuesta))
    
    print(''' EMPIEZA SEGUNDO LOOP ''')
    

    for i in range(x):
        print('De uno a X: ' + str(i))
        respuesta += x
        print('Se suma la X: ' + str(respuesta))
    
    print(''' EMPIEZA TERCER LOOP ''')

    for i in range(x):
        print('LOOP PRINCIPAL DE UNO A X: ' + str(i))
        # print('Es la respuesta inicial: ' + str(respuesta))
        for j in range(x):
            respuesta += 1
            respuesta += 1
            print('Empieza loop secundario:     ' + str(j))
            print('Se suma 2 por cada loop secundario: ' + str(respuesta))
    
    return respuesta

if __name__ == "__main__":
    f(5)