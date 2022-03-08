print('Gerador do n primeiros números ímpares positivos')

#leia o valor de n
n = int(input('Digite o valor de n: '))
#contador de ímpares impressos
i = 0
#primeiro número ímpar
impar = 1
#imprima os n primeiros ímpares, um por linha
while i < n:
    #imprima o próximo número ímpar
    print(impar)
    #incremente p contador
    i = i + 1
    #determine o próximo ímpar
    impar = impar + 2