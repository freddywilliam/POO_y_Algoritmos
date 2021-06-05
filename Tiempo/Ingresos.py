def opcion_uno(ingreso):

    egreso = 100
    ingreso -= egreso

    if ingreso <= 0:
        print( 'Tus egresos son: ' + str(ingreso) + ' Te recomiendo analizar tus finanzas.')

    else:
        print( 'Te sobra: ' + str(ingreso) + ' te recomiendo invertirlos en activos.')
        
    print('''
          Tus egresos personales son: 
        $20 Internet
        $10 Servicios online
        $20 Ocio
        $30 Emergencia
        $20 Gasto  ''')
        

def opcion_dos(ingreso):

    egresos = {}
    egresos_suma = 0

    print('Escribe "0" si acabaste. ')
    
    for i in range(1, 100):
        nombre = str(input('Escribe el nombre de tu egreso: '))
        
        if nombre == '0':
            break

        valor = int(input('Escribe el valor de tu egreso: '))

        egresos[nombre] = valor

    egresos_suma = sum(egresos.values())
    ingreso_egreso = ingreso - egresos_suma
    

    print(''' 
        
    Esta es tu lista:
        
        ''' )

    for keys, values in egresos.items():
        print('         ' + str(keys) + ': $' + str(values))

    if ingreso_egreso <= 0:
        print(''' 
        
        ''')
        print( 'El total de tus egresos es: ' + str(ingreso_egreso) + ' Te recomiendo analizar tus finanzas.')
     
    else:
        print(''' 
        
        ''')
        print( 'Tus ingresos son: ' + str(ingreso))
        print('Tus egresos son: ' + str(egresos_suma))
        print('Te quedan ' + str(ingreso_egreso) + ' para invertir o ahorrar.')

def run():

    ingreso = int(input('Dime tus ingresos: '))

    print(''' 
        ELIGE LAS OPCIONES
    1) Valores predeterminados
    2) Valores nuevos

        ''')

    opcion = int(input('''Quiero usar: '''))

    if opcion == 1:
        opcion_uno(ingreso)

    elif opcion == 2:
        opcion_dos(ingreso)
        
    elif opcion >= 3:
        print('Error')

if __name__ == "__main__":
    run()