n = int(input('Digite o número que você deseja obter a tabuada: '))
c = 1

print('-'*12)
while (c<11):
    r = n*c
    print('{} x {:2} = {}'.format(n,c,r))
    c = c + 1
print('-'*12)