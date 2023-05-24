#Programa para ler e sortear um nome

#primeiramente importar a bibi random

from random import choice

#Entrando com os dados a serem sorteados
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))

#Criando uma lista com os dados informados
lista = [a1,a2,a3,a4]

#usando a função random para escolher um elemento da lista
escolhido = choice(lista)

print(escolhido)
