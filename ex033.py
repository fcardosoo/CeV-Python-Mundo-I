# peça 3 números e diga qual é o maior
# qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

print('-=-' * 10)

# Considerarei n1 como o menor e após testarei

# verificar quem é o menor;

menor = n1
maior = n1

if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3

print('O menor valor é {}.'.format(menor))

# verificando o maior

if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

print('O maior valor é {}.'.format(maior))
print('-=-' * 10)
