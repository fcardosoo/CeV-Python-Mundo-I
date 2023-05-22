#ler o comprimento de 3 retas e
#diga se pode forma um triângulo

print('-=-'*10)
print('Analisando TRIÂNGULOS!!!')
print('-=-'*10)

r = float(input('Informe o valor da reta 1: '))
s = float(input('Informe o valor da reta 2: '))
t = float(input('Informe o valor da reta 3: '))

if r<(s+t) and s<(r+t) and t<(r+t):
    print('*'*35)
    print('É possível formar um triângulo!')
    print('*' * 35)
else:
    print('*' * 35)
    print('Não é possível formar um triângulo!')
    print('*' * 35)