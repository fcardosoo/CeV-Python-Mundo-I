c = float(input('Qual o comprimento da parede? '))
a = float(input('Qual a altura da parede? '))
area = c*a
t = area/2
print('A parede tem {}m de comprimento,\n'
      ' por {} metros de altura, totalizando \n'
      '{} metros quadrados. Você precisará \n'
      'de {} litros de tinta para realizar \n'
      'a pintura.'.format(c,a,area,t))