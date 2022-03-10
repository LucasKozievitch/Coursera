import math

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a, b, c)

def delta(a, b, c):
    return ((b ** 2)-(4 * a * c))

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    # raiz1 = (-b + math.sqrt(d)) / (2 * a)
    # raiz2 = (-b - math.sqrt(d)) / (2 * a)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('A única raiz é: ', raiz1)
    else:
        if d > 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('A raiz 1 é: ', raiz1)
            print('A raiz 2 é: ', raiz2)
        else:
            print('A equação não possui raízes reais.')

main()
