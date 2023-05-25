# Peça um número para o usuário
# informe se ele é par ou ímpar

from time import sleep

print('-=-'*10)
n = int(input('Digite um número inteiro: '))
print('-=-'*10)

print('Processando...')
sleep(3)

if n%2 == 0:
    print('*'*50)
    print('O número é PAR!!!')
    print('*' * 50)
else:
    print('*' * 50)
    print('O número é ÍMPAR!!!')
    print('*' * 50)