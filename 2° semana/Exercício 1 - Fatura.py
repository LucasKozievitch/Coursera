#Entrada de dados
nome_cliente = input('Digite o nome do cliente: ')
dia_vencimento = input('Digite o dia de vencimento: ')
mes_vencimento = input('Digite o mês de vencimento: ')
valor_fatura = input('Digite o valor da fatura: ')

#Saída de dados
print('Olá, {} '.format(nome_cliente),'\nA sua fatura com vencimento em {}'.format(dia_vencimento),
      'de {}'.format(mes_vencimento),'no valor de R$ {}'.format(valor_fatura),'está fechada.')