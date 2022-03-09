def resto(x, y):
    return x % y

x = int(input('Digite o número para saber se é divisível por 3: '))
y = 3

resultado = resto(x, y)

if resultado == 0:
    print('Fizz')

else:
    print(x)