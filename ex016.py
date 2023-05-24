# Criar um programa que leia um número real e mostre apenas a parte inteira

#Primeiramente devemos importar a funcinalidade truncar da bib Math

from math import trunc

n = float(input('Digite um número: '))

i = trunc(n)

print('A primeira forma é usar a função trunc: ', i)
print('Outra forma de exibir a parte inteira é converer o número em inteiro {}'.format(int(n)))
