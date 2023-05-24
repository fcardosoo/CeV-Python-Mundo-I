#Ler um nome e mostrar:
#O nome com todas em Maiúsculo/Minúsculo
#Contar a quant. de letras sem os espaços
#Contar quantas as letras do primeiro nome

nome = input("Digite um nome completo: ")
print('*'*50)
print('O nome em maiúsculo fica: {} '.format(nome.upper()))
print('O nome em minúsculo fica: {} '.format(nome.lower()))
print("O nome possui {} caracteres.".format(len(nome)))
nome1= nome.replace(" ","")
print('o nome possui {} caracteres sem espaço. '.format(len(nome1)))
div = nome.split()
print('O primeiro nome tem {} letras'.format(len(div[0])))