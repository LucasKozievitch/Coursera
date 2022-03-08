#Funções para os calculos
def perimetro (x):
    return 4 * x

def area (x):
    return x ** 2

#Entrada de dados
x = int(input('Digite o valor correspondente ao lado de um quadrado: '))

#Saída de dados
print('perímetro: {}'.format(perimetro(x)),'-', 'área: {}'.format(area(x)) )