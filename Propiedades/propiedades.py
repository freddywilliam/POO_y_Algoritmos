class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    def __getnombre(self):
        return self.__nombre
    
    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre= nombre
    
    def __setsalario(self, salario):
        self.__salario

    def __delnombre(self):
        del self.__nombre

    def __delsalario(self):
        del self.__salario

    nombre = property(fget=__getnombre, fset=__setnombre, fdel=__delnombre, doc='Soy la propiedad del 'nombre' ')
    salario = property(fget=__setsalario)
    empleado_uno =Empleado('Victor', 2000 )
    empleado_dos =Empleado('Sara', 3000)