v = float(input('Informe o valor disponível em Reais (R$): '))
cot = float(input('Qual a cotação atual do dolar?: '))
c = v/cot
print('Você pode comprar o total de US${:.3f}'.format(c))