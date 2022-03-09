print('Raízes de uma equação de segundo grau')
print('Equação: ax²+bx+c')
a = int(input('Digite o parâmetro a: '))
b = int(input('Digite o parâmetro b: '))
c = int(input('Digite o parâmetro c: '))

delta = (b**2)- 4*a*c
r1 = (-b + (delta**(1/2)))/(2*a)
r2 = (-b - (delta**(1/2)))/(2*a)

if delta > 0:
    if r1 < r2:
        print('as raízes da equação são {r1} e {r2}'.format(r1=r1, r2=r2))
    else:
        print('as raízes da equação são {r2} e {r1}'.format(r1=r1, r2=r2))

if delta == 0:
    print('a raiz dupla desta equação é', r1)
else:
    print('esta equação não possui raízes reais')
