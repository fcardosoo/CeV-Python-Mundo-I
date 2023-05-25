# Crie um algoritmo que sorteie um número entre
# 0 e 5 e peça para o usuário tentar adivinhar.
# após print na tela se o usuário acertou ou não.
import random
from time import sleep
print('-=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
n = int(input('Insira seu palpite: '))
print('Processando....')
sleep(3)
a = random.randrange(0,5)

if n==a:
    print('PARABÉNS, você acertou, eu pensei no número {}!!!'.format(a))
    print('-=-' * 30)
else:
    print('Perdeu!!! Eu pensei no número {}, não no número {}.'.format(a, n))
    print('-=-' * 30)

