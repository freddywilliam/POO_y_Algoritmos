class Humano:
    def __init__(self, edad, sexo, nombre):
        self.edad = edad
        self.sexo = sexo
        self.nombre = nombre

    def saluda(self, mensaje):
        print(mensaje)

       
pedro = Humano(23, 'Masculino', 'Pedro')
susana = Humano(22, 'Femenino', 'Susana')

pedro.saluda('Hola, mi nombre es ' + pedro.nombre + ' tengo ' + str(pedro.edad) + ' de edad.')
susana.saluda('Hola, mi nombre es ' + susana.nombre + ' tengo ' + str(susana.edad) + ' de edad.')


