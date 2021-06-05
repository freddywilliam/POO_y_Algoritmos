class Cliente:
    def __init__(self):
        self.__codigo = 4321
        # __codigo si tratamos de imprimir nos va a tirar error, pero si quito __ se podra ver.

    def __cuenta(self):
        print('Cuenta de procesamiento')

    def getcodigo(self):
        return self.__codigo

# Para poder llamar a __codigo necesito 
# la funcion getcodigo
    #  return self.__codigo
#  objeto.__nombreclase__nombre atributo
persona = Cliente()
print(persona._Cliente__codigo)
persona._Cliente__cuenta()