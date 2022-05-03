def primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input("Limite máximo: "))

n = 2
lista = []
while n < limite:
    if primo(n):
        lista.append(n)
    n = n + 1

print("\nA lista de números primos é: \n{}".format(lista))