frase='Curso em Vídeo Python'

print(frase[3])
print(frase[3:13])
print(frase[0:13])
print(frase[1:15:2])
print(frase[::2])

print('Oi')

print("""Hospitais de Manaus voltam a instalar câmaras 
frigoríficas Medida foi utilizada em abril, durante 
o ápice da pandemia; na última terça, o Amazonas atingiu
o maior número de internações em um único dia desde
a chegada da covid-19 no Estado""")

#EM PYTHON TUDO É OBJETO, desta forma é possivel usar
#o que foi criado com funções (.função).. EXEMPLO:
print('-'*50)

print(frase.count('O')) # contar o nr de O na frase
print(frase.upper().count('O')) # convertendo toda a frase para maiúsculo antes de contar
print(len(frase)) #contar o nr de caracteres na frase
print(frase.replace('Python', 'Android')) # mudar uma palavra por outra
print(frase.find('Curso')) #busca uma palavra na string *atenção a maiúsculo/minúsculo | A função mostra a posição da palavra
print(frase.find('curso')) # esta busca resultará -1, ou seja não encontrou a palavra com todas minúsculas
print(frase.lower().find('curso')) # este retornará ok, pois primeiro convertemos todas p/ minúsculo

#criando uma lista com a string
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2][3]) #Usando desta forma, a função busca na palavra 3 (lembrando que começa em ZERO) e a letra 4 (que começa em ZERO) desta palavra
