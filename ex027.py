# Leia o nome completo e indique o primeiro e o
#último nome

n = str(input('Digite o nome completo: ').title().strip())
nome = n.split()
print('Analisando a informação, seu primeiro nome é {}, e seu último nome é {}.'.format(nome[0], nome[len(nome)-1]))
