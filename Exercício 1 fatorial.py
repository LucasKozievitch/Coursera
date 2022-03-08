x = int(input('Digite um número natural a ser fatorado: '))
i = (x-1)
if x == 0:
    print(1)
while i > 0:
    if i >= 1:
        x = x*i
        i = (i-1)

print(x)