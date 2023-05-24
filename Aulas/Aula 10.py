#Estruturas de repetição

# 1º) Estrutura SE simples
nome = str(input('Qual o seu nome? ').capitalize().strip())
if nome == 'Fabiano':
    print('Que nome lindo você tem!!!')
print('Bom dia, {}!'.format(nome))

# 2º Estrutura SE composta (com o ELSE)
print('*'*30)
if nome == 'Fabiano':
    print('Que nome lindo você tem!!!')
else:
    print('Que nome normal você tem!')
print('Bom dia, {}!'.format(nome))

print('*'*30)

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
if m>=6:
    print('Sua nota foi {}, PARABÉNS!'.format(m))
else:
    print('Sua nota foi {}, ESTUDE MAIS!'.format(m))
print('*'*30)
