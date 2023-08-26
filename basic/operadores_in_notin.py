#nome = 'Lucas'
#print(nome[2])
#quando passo entre parentes do numero em q está o caracter ele me exibe esse char loca
#localizado na str 

nome = 'Lucas'
print('a' in nome) #retorne se a está entre as letras da variavel 'nome'

print('z' in nome)
print('sac' in nome)
print('cas' in nome)

nome = input("digite um nome :) ")
encontrar = input("digite oque deseja encontrar nesse nome: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')    
else:
    print(f'{encontrar} não está em {nome}')    




