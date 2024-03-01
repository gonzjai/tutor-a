# 1° se toma el problema que se va a calcular con un input  que se va a llamar problem

problem = input('Digita el problema a resolver =>\nEjemplo(2+2*4)\n=>')

# 2°   creo una lista sin elementos
#      luego itero el problema y añado cada caracter por separado a la lista
#      esto me facilitará su posterior análisis
#      le añado un item que me facilitará los calculos posteriores para iterar el problema
first_list = []      
for x in problem:     
    first_list.append(x)
first_list.append('')

#print(f'p_list => {first_list}')


# 3°  creo una lista sin elementos
#     itero la anterior lista que contiene todos los caracteres separados
#     añado en orden y por separado a la nueva lista los valores y los operadores 
#     -el if toma los valores de string que corresponden a números Y si en la siguiente
#        iteración encuentra otro valor numerico se lo añade al ya existente
#     -el elif toma los operadores, añade en orden el valor numerico terminado y el operador

final_list = []
number = 0
for x in first_list:
    if x.isdigit() == True:
        if type(number) == type(0):
            number = x
        elif type(number) == type(''):
            number = number + x
    elif x.isdigit() == False:
        final_list.append(number)
        final_list.append(x)
        number = 0
#print(f'p2_list => {final_list}')


# 4° creo un rango de valores para iterar la operación 
#    el rango lo hice de forma que la iteración sea comoda
#    el rango está determinado desde el 1 hasta el numero se datos de la lista dividido en 2
#    lo cual me genera un rango que contiene el número de operadores usados

range = list( range(1, int(len(final_list) / 2)))
#print(f'range => {range}')


# 5° Realizo la operación con los datos ya depurados
#    hago el uso de un ciclo for determinado por el numero de operadores empleados
#   -el if toma la primera opción que está determinada por el valor el la posición 0
#      y el valor el la posición 2 (x-1) y (x+1) respectivamente
#      y el operador está en la pocicion 1 (x)
#   -el elif toma el resto de opciones que es el resultado anterior 
#      operado con el signo en la posición ((x*2)-1)
#      y el valor en la posición (x*2)

counter = 0
for x in range:
    if counter == 0:
        numero_1 = float(final_list[(x-1)])
        numero_2 = float(final_list[(x+1)])
        if final_list[x] == '+':
            result = numero_1 + numero_2
            counter += 1
        if final_list[x] == '-':
            result = numero_1 - numero_2
            counter += 1
        if final_list[x] == '*':
            result = numero_1 * numero_2
            counter += 1
        if final_list[x] == '/':
            result = numero_1 / numero_2
            counter += 1
    elif counter > 0:
        if final_list[(x*2)-1] == '+':
            numero_3 = float(final_list[(x*2)])
            result = result + numero_3
        elif final_list[(x*2)-1] == '-':
            numero_3 = float(final_list[(x*2)])
            result = result - numero_3
        elif final_list[(x*2)-1] == '*':
            numero_3 = float(final_list[(x*2)])
            result = result * numero_3
        elif final_list[(x*2)-1] == '/':
            numero_3 = float(final_list[(x*2)])
            result = result / numero_3
print(f'result => {result}')