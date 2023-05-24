# Ler 4 nomes e sortear a ordem.

from random import shuffle

n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))

lista = [n1,n2,n3,n4]

#Embaralhando a lista com a função SUFFLE

shuffle(lista)

print('A ordem de apresentação será: \n',
      lista)
