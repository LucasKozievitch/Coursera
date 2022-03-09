def resto(x, y):
    return x % y

x = int(input('Digite o número para saber se é divisível por 5: '))
y = 5

resultado = resto(x, y)

if resultado == 0:
    print('Buzz')

else:
    print(x)