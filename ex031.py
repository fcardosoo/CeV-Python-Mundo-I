#Perguntar a distância de uma viagem
# calc o preço cobrando $0,50/KM em viagens
#até 200KM e $0,45 p/ viag acima de 200km

d = int(input('Qual a distância até se destino? '))

if d<=200:
    print('*'*50)
    print('Até o destino são {}Km, com valor de R$0,50/Km, \nficando a passagem R${}.'.format(d, d*0.5))
    print('*' * 50)
else:
    print('*' * 50)
    print('Até o destino são {}Km, com valor de R$0,45/Km, \nficando a passagem R${}.'.format(d, d * 0.45))
    print('*' * 50)
