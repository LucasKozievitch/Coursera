# Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos,
#  indicando também a mutiplicidade de cada fator.

# SOLUÇÃO 1
def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    while n != 1:
        # conta a multiplicidade de fator em n
        mult = 0
        while n%fator == 0:
            n = n / fator
            mult = mult + 1

        # imprime a multiplicade do fator
        if mult != 0:
            print("fator %d multiplicidade %d" %(fator, mult))

        fator = fator + 1

main() # chamada da função principal


#-------------------------------------------------------------------

# SOLUÇÃO 2
def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    while n != 1:
        # conta a multiplicidade de fator em n
        n, mult = fatora(n, fator)

        # imprime a multiplicade do fator
        if mult != 0:
            print("fator %d multiplicidade %d" %(fator, mult))

        fator = fator + 1

def fatora(n, f):
    ''' (int, int) -> int, int
        fatora n por f. Retorna o novo valor de n e
        a multiplicidade de f.
    '''
    mult = 0
    while n%f == 0:
       n = n / f
       mult = mult + 1
    return n, mult

main() # chamada da função principal


#-------------------------------------------------------------------

# SOLUÇÃO 3
def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    mult = 0;

    while n != 1:
        # conta a multiplicidade de fator em n
        if n%fator == 0:
            n = n / fator;
            mult = mult + 1;
        else:
            # imprime a multiplicade do fator
            if mult != 0:
                print("fator %d multiplicidade %d" %(fator, mult))
                mult = 0

            fator = fator + 1

    # imprime a multiplicade do ultimo fator
    if mult != 0:
        print("fator %d multiplicidade %d" %(fator, mult))

main() # chamada da função principal