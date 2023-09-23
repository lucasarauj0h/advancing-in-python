## Avaliação e Média da Nota de Filmes
''''
## Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1. Cada produto deve ter um preço e um nome.
2. A classe deve ter um método construtor e o método dundle str.
3. A classe deve ter um método para desconto. O método deve receber o desconto em
percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.
'''

import random

class Product():
    
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    def discount(self, percentage):
        if percentage > 1:
            percentage /= 100
            self.__price -= (self.__price*percentage)
        else:
            self.__price -= (self.__price*percentage)            

    def __str__(self):
        return f'Nome do produto: {self.__name}\nPrice: {self.__price}'
    
    


# for i in range(10):
#     nota = random.randrange(3,5)
#     print(nota)
#     movie_mario.users_assessment(nota)
#     movie_mario.techinal_sheets()

discount = random.randrange(100) / 100
print(discount)
discount = 75
feijao = Product("Feijão",10,5)
feijao.discount(discount)
print(feijao)
