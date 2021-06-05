class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Caminando')
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Pedaleando')

def main():
    persona = Persona('Pedro')
    persona.avanza()

    ciclista = Ciclista('Juan')
    ciclista.avanza()

if __name__ == "__main__":
    main()