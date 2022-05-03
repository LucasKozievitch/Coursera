

def minmax (temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def maxima (temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def minima (temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

#-----------------------------------------------------------------------

def testa_pontual1(temp, valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado,
              ". Valor calculado: ", valor_calculado)

def testa_pontual2(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado,
              ". Valor calculado: ", valor_calculado)

#-----------------------------------------------------------------------

def testa_min():
    print("Iniciando os testes.")
    testa_pontual2([0], 0)
    testa_pontual2([0, 0, 0, 0, 0], 0)
    testa_pontual2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    testa_pontual2([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes")

def testa_max():
    print("Iniciando os testes.")
    testa_pontual1([0], 0)
    testa_pontual1([0, 0, 0, 0, 0], 0)
    testa_pontual1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    testa_pontual1([-15, -12, 0, 20, 30], 30)
    print("Finalizando os testes")

#-----------------------------------------------------------------------

testa_min()
testa_max()
minmax([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])