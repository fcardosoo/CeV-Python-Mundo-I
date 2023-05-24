from math import sqrt,floor
import random

#Para importar uma biblioteca externa ex. bib emoji
import emoji

print(emoji.emojize('Olá Mundo! :sunglasses:', use_aliases=True))
print(emoji.emojize('Olá Canadá :earth_americas:', use_aliases=True))

print('='*20)

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))



#________________
#Gerando números aleatórios com a bib 'random'

num = random.random()
num2 = random.randint(1,10)

print(num,'\n', num2)