def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():
        # Acciones adicionales que decoran

        print('Vamos a realizar una operacion: ')
        funcion_parametro()

        # Acciones adicionales que decoran

        print('Hemos terminado la operacion. ')

    return funcion_interior

@funcion_decoradora
def suma():
    print(15 + 20)

@funcion_decoradora
def resta():
    print(15 - 10)
suma()
resta()