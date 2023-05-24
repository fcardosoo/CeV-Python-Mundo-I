#Trabalhando com cores em PYTHON

# O código ANSI

# Fonte: 0 nenhum; 1 bold; 4 underline; 7 negative
# Texto: 30 white, 31 red, 32 green, 33 yel, 34 blue, 35 purple, 36 light blue, 37 grey
# Back:  40 a 47 vide acima

#\033[ style; text; back m]

############ TESTE #########
print('-=-'*15)
print('\033[0;30;41m TESTE\033[m')
print('\033[4;33;46m TESTE\033[m')
print('\033[1;35;43m TESTE\033[m')
print('\033[0;30;42m TESTE\033[m')
print('\033[m TESTE\033[m')
print('\033[7;30m TESTE\033[m')
print('-=-'*15)

print('\33[1;31;43m Olá Mundo!\033[m')
print('-=-'*15)

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('-=-'*15)

#Mostrando as cores de outra forma
nome = 'Fabiano'
print('Olá {}{}{}, muito prazer em te conhecer!!!'.format('\033[4;31m',nome ,'\033[m'))