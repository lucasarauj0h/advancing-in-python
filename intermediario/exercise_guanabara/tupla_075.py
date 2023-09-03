n = (int(input('Digite o numero 1: ')),
     int(input('Digite o numero 2: ')),
     int(input('Digite o numero 3: ')),
     int(input('Digite o numero 4: ')))

print(f'você digitou os numeros {n}')
print(f'você digitou o numero 9 - {n.count(9)} vezes')
print(f'a primeira vez que o 3 aparece é em [{n.index(3)}]')

for i in n:
    if i % 2 == 0:
        print(f'Número par: {i}')