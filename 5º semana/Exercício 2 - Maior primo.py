
n = int(input('Digite um número inteiro: '))
lista = []

for i in range(1, n+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            lista.append(i)

print(max(lista))
