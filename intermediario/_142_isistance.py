# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set): #caso seja true o isistance, ele vai exibir o item set.
        item.add(7) #nesse caso por ser set, eu posso usar o .add, mas 
        #nem todos dessa lista permite esse tipo, por isso temos que verificar!
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        item.upper() 
        print(item.upper(), isinstance(item.upper(), str))

    elif isinstance(item, (int, float)):
        print(item, isinstance(item,(int)))

    else:
        print('outro')
        print(item)

    