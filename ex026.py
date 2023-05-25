#Leia uma frase e indique a quantidade de letras 'a'
#A posição que ela aparece na primeira vez
#A posição que ela aparece na última vez

f = str(input('Digite algo: ')).lower().strip()

print('A letra -a- aparece {} vezes.'.format(f.count('a')))
print('A primeira letra -a- apareceu na posição {}.'.format(f.find('a')+1))
print('A última letra -a- apareceu na posição {}.'.format(f.rfind('a')+1))