#Tipos primitivos
n1=int(input('Digite um número: '))
n2=int(input('Digite o segundo número: '))
n3=input('Digite algo: ')
s=n1+n2

print('A soma entre ', n1, ' e ', n2, 'vale: ',s)

# print usando vaiáveis{}
print('A soma entre {} e {} vale: {}'.format(n1,n2,s))

# Mostando o tipo primitivo da variável
print(type(n1))

#Verificando o que foi digitado em n3
print(type(n3))
print(n3.isnumeric())

#Verificando se n3 é letra (alfabeto)
print(n3.isalpha())