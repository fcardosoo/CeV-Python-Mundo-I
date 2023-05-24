#Aula sobre cadeia de caracteres

frase = 'Curso em Vídeo Python'

# Fatiamento

#Ex.: frase[9] busca o nono caracter

print(frase[9])

# Fatiamento 'frase[9:13]' este intervalo chama-se range
print(frase[9:13])
print(frase[9:21])

# Fatiamento saltando de 2 em 2 casas

print(frase[9:21:2])

# Fatiamento começando no início até :X

print(frase[:5])

# Fatiamento iniciando em X até o final

print(frase[15:])

# Fatiar iniciando em X::3 até o final de 3 em 3
print(frase[9::3])

######## Analisar uma String #########
print('*'*50)
print(len(frase))
print(frase.count('o'))

# Contando do 0 ao 13 apenas a letra 'o'
print(frase.count('o',0,13))

#Encontrando parte do texto e indicando o inicio
print(frase.find('deo'))

#Quando o sistema não encontra a palavra retorna -1
print(frase.find('Android'))

# Acha valor e retorna True/False
print('Curso' in frase)

#Alterar uma palavra na String com o REPLACE
print(frase.replace('Python','Android'))

#Alterar para maúscula/minúscula
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

#Removendo espaços desnecessários antes/depois
frase2 = '   Aprenda Python  '

print('*'*50)

print(frase2)
print(frase2.strip())

#Para remover apenas espaços no lado direito
print(frase.rstrip())

#Para remover apenas espaços no lado esquerdo
print(frase.lstrip())

print('*'*50)

########## DIVIDIR STRING ############

# Utilizando o SPLIT

frase3 = ('Curso em Vídeo Python')
print(frase.split())

########## JUNÇÃO STRING ############

# Utilizando o JOIN

print('-'.join(frase))