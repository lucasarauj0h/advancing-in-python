from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
ordenado = sorted(n)
print(f'Maior número:{ordenado[4]}')
print(f'Menor número:{ordenado[0]}')
print(f'Números: {n}')

print(f'Maior número:{max(n)}')
print(f'Menor número:{min(n)}')
