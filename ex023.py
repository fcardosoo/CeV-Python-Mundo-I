#Leia um número de até 4 digitos
#[ de 0 a 9999] e mostre na tela
# unid, dez, cent e milhar

n = int(input('Digite um número de até 4 dígitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número {} '.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))