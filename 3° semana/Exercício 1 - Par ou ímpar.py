def resto(x, y):
    return x % y

x = int(input('Digite o número para saber se é par ou ímpar: '))
y = 2

resultado = resto(x, y)

if resultado == 0:
    print('par')

else:
    print('ímpar')