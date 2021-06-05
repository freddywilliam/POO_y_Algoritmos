class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self, temperatura):
        print('Estamos llenando el tanque con agua ' + temperatura)
    
    def _agregar_jabon(self):
        print('Agregando jabon')

    def _lavar(self):
        print('Lavando')

    def _centrifugar(self):
        print('Centrifugando')

if __name__ == "__main__":

    lavadora = Lavadora()
    lavadora.lavar()

