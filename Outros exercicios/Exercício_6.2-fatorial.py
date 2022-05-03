# Função fatorial que recebe como parâmetro 
# um número inteiro k, k >= 0, e retorna k!.

def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat

# testes
print("Exemplos de fatoriais!!")
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("17! =", fatorial(17))
print("------------------------\n")

k = int(input("Digite um número a ser fatorado: "))
print('{}! ='.format(k), fatorial(k))