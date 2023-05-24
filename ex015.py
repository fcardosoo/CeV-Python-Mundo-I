# Alugando carros! Calcular valor a pagar
#considere $60/dia + $0,15/km

print('-'*50)
print('Seja bem vindo a tela de cálculo do valor de aluguel!')

print('-'*50)
print('Diárias R$60,00 e R$0,15 por Km rodado.')
print('-'*50)

d = int(input('Informe quantos dias o carro ficou alugado: '))
kmi = int(input('Informe a Kilometragem Inicial: '))
kmf = int(input('Informe a Kilomtragem Final: '))
t = d*60 + ((kmf-kmi)*0.15)

print('-'*50)
print('O veículo rodou {}km, \n'
      'por {} dias, \n'
      'Totalizando: \n'
      'Aluguel: R${} \n'
      'Kilometro rodado: R${} \n'
      'Total: R${:.2f} a pagar.'.format(kmf-kmi,d,d*60,(kmf-kmi)*0.15,t))

print('-'*50)
print('Obrigado pela preferência!!!')