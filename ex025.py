#Leia um nome completo e indique
#se há a presença de 'SILVA' em qualquer ponto

n = str(input('Digite um nome: ').strip().upper())
print('Seu nome tem SILVA? {}'.format('SILVA' in n))
