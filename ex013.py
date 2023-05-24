s = float(input('Digite o valor do salário em R$: '))
a = float(input('Digite o valor do dissídio em %: '))
aum = s * (a/100)

print('O seu salário atual é R${} \n'
      'o dissídio é de {}%, seu \n'
      'novo valor salarial é de R${:.2f}'.format(s,a,s+aum))