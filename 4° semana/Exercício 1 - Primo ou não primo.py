n = int(input('Digite um número inteiro: '))

x = range(1, n+1, 1)

lista = list(x)
lista1 = []

for x in lista:
    if n % x == 0:
        lista1.append(x)
len(lista1)

if len(lista1) != 2:
    print('não primo')

else:
    print('primo')