import os
print("\n" * os.get_terminal_size().lines)
import math #biblioteca que importa elementos presente na matemática

print(math.pi)
print(f'{math.pi:.2f}') #Pi da matematica
print(math.e)
print(f'{math.e:.2f}') #valor do Euller

num = 10.4
print(math.ceil(num)) #arredonda p/ cima - num inteiro
print(math.floor(num)) #arredonda p/ baixo - num inteiro

#fatorial de um num
print(math.factorial(5))
#potencia
print(math.pow(5,2))
#raiz quadrada
print(math.sqrt(169))

#mdc (menor divisor comum)
print(math.gcd(55,80))

#logaritmo
print(math.log(28,21))