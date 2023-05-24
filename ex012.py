p = float(input('Informe o preço do produto: '))
d = float(input('Informe o desconto em valor %: '))
desc = p*(d/100)
pn = p-desc

print('O produto custa {}, \n'
      'mas neste momento possui um \n'
      'desconto especial de {}%, \n'
      'ficando por R${:.2f}.'.format(p, d, pn))