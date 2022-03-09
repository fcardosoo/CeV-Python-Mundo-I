v1=input('Digite uma palavra: ')
n1=int(input('Digite o primeiro nr: '))
n2=int(input('Digite o segundo nr: '))


print('O que foi digitado são letras? ',v1.isalpha())
print('O que foi digitado são números? ',v1.isnumeric())
print('O que foi digitado é alfanumérico? ',v1.isalnum())
print('O que foi digitado está em maiúsculo? ',v1.isupper())
print('O que foi digitado está em minusculo? ',v1.islower())
print('O que foi digitado é apenas espaços? ', v1.isspace())
print('O que foi digitado está Capitalizado? ',v1.istitle())

#opções de print
print('Prazer em te conhecer {:^20}!'.format(v1))
print('Prazer em te conhecer {:*^20}!'.format(v1))
print('Prazer em te conhecer {:=^20}!'.format(v1))
print('Prazer em te conhecer {:>20}!'.format(v1))
print('Prazer em te conhecer {:<20}!'.format(v1))

#calculos
s=n1+n2
m=n1*n2
d=n1/n2
d1=n1//n2
e=n1**n2
print('A soma é {}\n, o produto é {} \ne a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira é {} \ne a potência é {}'.format(d1, e))

#para as duas linhas acima aparecerem como uma linha só
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e a potência é {}'.format(d1, e))
