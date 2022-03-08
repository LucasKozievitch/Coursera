#leia o valor de n
n = int(input('Digite um número inteiro: '))

#definição da função soma
def getSum(n):
    sum=0
    while (n != 0):
        sum = sum + (n%10)
        n = n//10
    return sum
print (getSum(n))