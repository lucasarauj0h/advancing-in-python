"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

var = 'olá mundo!'
print(var[5])
print(var[-4])
print()
print(var[4:])
print(var[4:8])
print(var[0:5])
print()

#a função len conta a quantidade de caracteres
print(len(var[0])) #como eu selecionei só 1 variavel para exibir, o len vai retornar 1 
print(len(var)) #conta quantos char tem no var.
print(var[0:print(len(var))])
print(var[0:print(len(var)):2]) #intervalo de 2 em 2

