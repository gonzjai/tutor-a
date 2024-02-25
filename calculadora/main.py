# con ésta función me aseguro de explicar como funciona el programa 

def reglas():
    print(' ')
    print('para sumar usa +')
    print('para restar -')
    print('para multiplicar *')
    print('para dividir / ')
    print('las operaciones se realizan en el orden que las escribas')
    print('no puedes repetir una misma operación')
    print('no dejes espacios entre operaciones, ejemplo (2*2+3)')
    print(' ')


# con ésta función recolecto los el index de cada operador usado
# y le aplico un sor para que queden en su debido orden
    
def recolectar_operadores(operacion):
    operadores = []
    if '+' in operacion:
        operadores.append(operacion.index('+'))
    if '-' in operacion:
        operadores.append(operacion.index('-'))
    if '*' in operacion:
        operadores.append(operacion.index('*'))
    if '/' in operacion:
        operadores.append(operacion.index('/'))
    operadores.sort()
    return operadores


# con esta funcion realizo las operaciones que especifiquen

def calculos(operation,signos):
    
    counter = 0
    for x in range(0,len(signos)):
        # este if es solo para la primera ves del siclo for
        # con este if me aseguro de separarlo en dos posibilidades
        # 1° que la cantidad de signos que hay en el ejercicio sea > 1
        # 2° que la cantidad de signos que hay en el ejercicio sea = 1
        if counter == 0:
            if not (len(signos) == 1):
                if operation[signos[0]] == '+':
                    calculo = int(operation[0:signos[0]]) + int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '-':
                    calculo = int(operation[0:signos[0]]) - int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo                    elif operation[signos[0]] == '*':
                    calculo = int(operation[0:signos[0]]) * int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '/':
                    calculo = int(operation[0:signos[0]]) / int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
            elif len(signos) == 1:
                if operation[signos[0]] == '+':
                    calculo = int(operation[0:signos[0]]) + int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '-':
                    calculo = int(operation[0:signos[0]]) - int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '*':
                    calculo = int(operation[0:signos[0]]) * int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '/':
                    calculo = int(operation[0:signos[0]]) / int(operation[signos[0]+1:])
                    to_continue = calculo
            
            # este if se usa cuando el siclo for se ejecuta mas de una vez
            # se divide en dos posibilidades ya que al finalizar el ciclo elimino 
                   # de la lista signos el primer elemento
            # 1° que la cantidan de signos que faltan por iterar sea = 1
            # 2° que la cantidad de signos que falta por iterar sea > 1       
        if not (counter == 0):
        
            if len(signos) == 1:
                if operation[signos[0]] == '+':
                    calculo = to_continue + int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '-':
                    calculo = to_continue - int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '*':
                    calculo = to_continue * int(operation[signos[0]+1:])
                    to_continue = calculo
                elif operation[signos[0]] == '/':
                    calculo = to_continue / int(operation[signos[0]+1:])
                    to_continue = calculo

            if not (len(signos) == 1):
                if operation[signos[0]] == '+':
                    calculo = to_continue + int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '-':
                    calculo = to_continue - int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '*':
                    calculo = to_continue * int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '/':
                    calculo = to_continue / int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo    
        signos.pop(0)
        counter += 1
    return to_continue






def calculadora():
    para_iniciar = input('¿Quieres hacer algún calculo?(si ó no)')

    

    if para_iniciar == 'si':
                               # propongo las reglas de uso 
        reglas()              
        
                               # ingresa el problema
        operation = input('ingresa tu operación =>')
                 
                               # recolecto los operadores usados con su respectivo index
        signos = recolectar_operadores(operation)
        
        calculo_total = calculos(operation,signos)
        print(calculo_total)
        
        

calculadora()
            


                




           






















