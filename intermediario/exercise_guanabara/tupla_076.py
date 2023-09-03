listagem = ('Lápis', '1.75', 
            'Borracha', '2.00', 
            'Caderno', '15.90', 
            'Estojo', '25.00', 
            'Transferidor', '4.20',
            'Compasso', '9.99', 
            'Mochila', '120.32', 
            'Caneta', '22.30', 
            'Livro', '34.90')
print("Item ------------------ Preço: ")
for item in range(len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:<20}', end='')
    else: 
        print(f'R$ {listagem[item]:>7}')