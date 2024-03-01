#input('Digita el problema a resolver =>\nEjemplo(2+2*4)\n=>')

problema = '22*444+3333*99999'     

p_list = []
for x in problema:
    p_list.append(x)
p_list.append('')

print(f'p_list => {p_list}')

# itero la lista y tomo los valores completos más los signos en una lista ordenada
p2_list = []
number = 0
for x in p_list:
    if x.isdigit() == True:
        if type(number) == type(0):
            number = x
        elif type(number) == type(''):
            number = number + x
    elif x.isdigit() == False:
        p2_list.append(number)
        p2_list.append(x)
        number = 0
print(f'p2_list => {p2_list}')


# creo un rango de valores para iterar la operación
range = list( range(1, int(len(p2_list) / 2)))
print(f'range => {range}')


# comienzo a iterar la operación en base a
counter = 0
for x in range:
    if counter == 0:
        numero_1 = float(p2_list[(x-1)])
        numero_2 = float(p2_list[(x+1)])
        if p2_list[x] == '*':
            result = numero_1 * numero_2
            counter += 1
    elif counter > 0:
        if p2_list[(x*2)-1] == '+':
            numero_3 = float(p2_list[(x*2)])
            result = result + numero_3
        elif p2_list[(x*2)-1] == '*':
            numero_3 = float(p2_list[(x*2)])
            result = result * numero_3
print(f'result => {result}')