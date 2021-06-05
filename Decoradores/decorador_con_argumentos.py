def funcion_decoradora(funcion_parametro):
    
            # El  *args sirve para indicar que se va a ingresar algunos argumentos
            #  El *kworgs sirve para indicar que en la funcion se ingresan paralabras claves junto al valor.
            #  Ejemplo  def color(primer=rojo)
   
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran

        print('Vamos a realizar una operacion: ')
        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran

        print('Hemos terminado la operacion. ')

    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

# Para la siguiente funcion necesito **kwargs
# pow = potencia = pow(base, exponente)

def potencia(base, exponente):
    print(pow(base, exponente))

suma(8,10,20)
resta(20,10)
potencia(5, 3)