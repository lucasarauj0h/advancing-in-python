"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Lucas'  
preco = 10086
variavel = '%s o preço é %.2f' % (nome, preco)
print(variavel)
variavel2 = 'o hexadecimal de %f é %X' % (preco, preco) #hexadecimal só funciona com int 
print(variavel2)