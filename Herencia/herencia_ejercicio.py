class Motor:
    def __init__(self, estado):
        self.estado = estado
      
    def funcion(self):
        if self.estado == 'activo':
            print('Encendiendo vehiculo')
    
class Carro(Motor):
    def __init__(self, estado):
        super().__init__(estado)


class Moto(Motor):
    def __init__(self, estado):
        super().__init__(estado)

if __name__ == "__main__":
   
    moto = Moto(estado='activo')
    print(moto.funcion())
  
    carro = Carro(estado='activo')
    print(carro.funcion())

