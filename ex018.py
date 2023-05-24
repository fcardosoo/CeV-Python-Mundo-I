#Programa para ler um ângulo qualquer e retornar os valores
#de seno, cosseno e tangente

import math

# Primeiramente devemos converter o angulo de graus para radianos
a = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('Para o ângulo {} \n'
      'O SENO é {:.3f}, \n'
      'O COSENO é {:.3f}, e \n'
      'A TANGENTE é {:.3f}.'.format(a, seno, cos, tan))