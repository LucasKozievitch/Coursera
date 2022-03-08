print('Coordenadas do primeiro ponto')
x1 = int(input('Digite o valor de x1: '))
y1 = int(input('Digite o valor de y1: '))

print('Coordenadas do segundo ponto')
x2 = int(input('Digite o valor de x2: '))
y2 = int(input('Digite o valor de y2: '))

d = (((x1 - x2)**2)+((y1 - y2)**2))**(1/2)

if d >= 10:
    print('longe')

else:
    print('perto')