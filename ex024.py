#Leia o nome de uma cidade e imprima se a cidade começa ou
#não com a palavra 'SANTO'

c = str(input('Digite o nome de uma cidade: '))
c = c.strip()
c = c.upper()

print(c[:5]=='SANTO')