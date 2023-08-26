"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

var = 'abc'
print(f'{var: >10}') #: [espaço] >10 -> digo para colocar 10 espaços a esquerda da var.
print(f'{var:X<10}') #: [X]<10 -> preencha o lado direito com 10 X's
print(f'{1556468.89789:,.2f}')

