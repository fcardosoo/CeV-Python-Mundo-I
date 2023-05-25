#informe o salario, se for até
#$1250 aumento de 15%, senão 10%

s = float(input('Informe o salário em R$: '))
a = str('10%')
b = str('15%')

if s > 1250:
    print('*'*50)
    print('O seu salário de R${}, será reajustado em {}, \n'
          'passando ao valor de {:.2f}.'.format(s, a, s*1.1))
    print('*' * 50)
else:
    print('*' * 50)
    print('O seu salário de R${}, será reajustado em {}, \n'
          'passando ao valor de {:.2f}.'.format(s, b, s * 1.15))
    print('*' * 50)
