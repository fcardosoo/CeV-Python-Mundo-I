# Criar algoritmo que solicita a velocidade do carro
# Se velicidade>80Km/h então multar em $7 por kmh acima
# do limite.

from time import sleep

v = float(input('Informe a velocidade atual em KM/H: '))
l = float(input('Informe a velocidade máxima da pista: '))

print('Processando.....')
sleep(3)

if v<=l:
    print('*'*50)
    print('God trip! Drive safely!')
    print('*' * 50)
else:
    print('*' * 50)
    print('Você ultrapassou a velocidade da pista de {}Kmh,\nvocê será multado em R${:.2f}.'.format(l, (v-l)*7))
    print('*' * 50)