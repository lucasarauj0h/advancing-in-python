lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

#print(lista)
#como eu faria isso em list comprehension?
# lista = [(lista.append((x,y)) for y in range(3) for x in range(3))]
# print(list(lista))
lista = [
    (x,y) #o que vai ser incluido na minha memoria 
    #a primeira linha ou o lado esquerdo do for é usado para o mapeamento, nesse
    #caso estamos mapeando uma tupla xy
    for x in range(3)
    for y in range(3)
    #isso resulta para nos um for dentro do outro. 
]
print(lista)
#lista = [n for n in range(10) if n<5] 

# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for key, value in produto.items():
    print(key,value)
print()

dc = {
    key: value.upper()
    if isinstance(value, str) else value #estou mapeando. se o valor for str inclua .upper()
    #n faça nada, caso nao seja str, o value n vai atribuir o .upper()
    for key, value in produto.items()
    if key == 'categoria' #só vou incluir o item q for igual a categoria, é um filtro
}
print(dc)