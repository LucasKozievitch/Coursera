def resto(x, y):
    return x % y
def resto1(x, y):
    return x % y1

x = int(input('Digite o número para saber se é divisível por 3 e 5: '))
y = (3)
y1 = (5)

resultado = resto(x, y)
resultado1 = resto1(x, y1)

if resultado == 0 and resultado1 == 0:
    print('FizzBuzz')

else:
    print(x)