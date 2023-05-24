#Calcular a hipotenuza

cat1 = float(input('Digite o valor do cateto A: '))
cat2 = float(input('Digite o valor do cateto B: '))

# é possível calcular usando apenas as aplicações matemáticas
hyp1 = (cat1**2 + cat2**2)**(1/2)

#A segunda maneira é importar a função pow da bib math
from math import pow
hyp2 = pow((pow(cat1, 2) + pow(cat2, 2)),(1/2))

# Outra forma é importando a função hypot
from math import hypot
hyp3 = hypot(cat1, cat2)

print('='*70)
print('Calculando a hipotenusa sem usar função: {}'.format(hyp1))
print('-'*70)
print('Calculando a hipotenusa com a função pow: {}'.format(hyp2))
print('-'*70)
print('Calculando a hypotenuza com a função hypot: {}'.format(hyp3))
print('='*70)