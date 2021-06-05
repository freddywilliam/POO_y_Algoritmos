class Cocineta:
    def __init__(self):
        pass

    def cocinar(self):
        self._estado()
        self._configuracion()
        self._apagado()

    def _estado(self, electricidad='Si hay electricidad', voltaje='bajo'):
        print('Si hay electricidad para cocinar')
        voltaje = 'bajo'

    def _configuracion(self, potencia=0):
            potencia = 3
            voltaje = 'alto'
            print('La estufa esta encendida a una potencia de ' + str(potencia) + ' (' + voltaje + ')')
    def _apagado(self):
        print('La comida esta lista. La cocineta esta apagada')

if __name__ == "__main__":
    cocineta = Cocineta()
    cocineta.cocinar()
