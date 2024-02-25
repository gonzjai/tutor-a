def reglas():
    print(' ')
    print('para sumar usa +')
    print('para restar -')
    print('para multiplicar *')
    print('para dividir / ')
    print('no puedes repetir una misma operación')
    print('no dejes espacios entre operaciones, ejemplo (2*2+3)')
    print(' ')

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

def un_calculo(operation,signos):
    if len(signos) == 1:
        for x in range(0,len(signos)):
            if len(signos) == 1:
                if operation[signos[0]] == '+':
                    calculo = int(operation[0:signos[0]]) + int(operation[signos[0]+1:])
                elif operation[signos[0]] == '-':
                    calculo = int(operation[0:signos[0]]) - int(operation[signos[0]+1:])
                elif operation[signos[0]] == '*':
                    calculo = int(operation[0:signos[0]]) * int(operation[signos[0]+1:])
                elif operation[signos[0]] == '/':
                    calculo = int(operation[0:signos[0]]) / int(operation[signos[0]+1:])
    print(calculo)
    return calculo

def mas_calculos(operation,signos):
    if len(signos) > 1:
        counter = 0
        for x in range(0,len(signos)):
            if counter == 0:
                if operation[signos[0]] == '+':
                    calculo = int(operation[0:signos[0]]) + int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '-':
                    calculo = int(operation[0:signos[0]]) - int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '*':
                    calculo = int(operation[0:signos[0]]) * int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
                elif operation[signos[0]] == '/':
                    calculo = int(operation[0:signos[0]]) / int(operation[signos[0]+1:signos[1]])
                    to_continue = calculo
            
            
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
        print(to_continue)
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
        
        if len(signos) == 1:
            resultado1 = un_calculo(operation,signos)
        else:
            resultado2 = mas_calculos(operation,signos)
        
        

calculadora()
            


                




           






















