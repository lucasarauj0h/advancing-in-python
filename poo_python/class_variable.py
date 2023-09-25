## Avaliação e Média da Nota de Filmes
''''
Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. 
Segue o escopo das funcionalidades:

1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um 
filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da 
classe.
2. Assim que uma avaliação for realizada, deve ser incrementado o total de
avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.
3. Para cada filme ter uma nota de avaliação média que consiste na divisão
do total de avaliação pelo total de avaliadores.
'''

import random

class Movie():
    platform = "OneBitFilms"
    def __init__(self, name, assessment, users):
        self.__name = name
        self.__assessment = assessment
        self.__users = users
        self.__allNote = assessment
    def __str__(self):
        return f'Nome do filme: {self.name}'
    
    def users_assessment(self, note):
        self.__users += 1
        self.__allNote += note
        self.__assessment = (self.__allNote / self.__users)

    def techinal_sheets(self):
        print("#"*30)
        print("Dados do filme -> ")
        print(f'Plataforma: {Movie.platform}') #variavel da minha classe, diferente da 
        #variavel de instancia; elas são fixas e não vao mudar de acordo com o objeto
        #(normalmente não), mas é possivel muda-los sim!
        print(f'Nome: {self.__name}')
        print(f'Média de notas: {self.__assessment}')
        print(f'Avaliações: {self.__users}')
        
movie_mario = Movie("Mario", 0, 0)

for i in range(10):
    nota = random.randrange(3,5)
    print(nota)
    movie_mario.users_assessment(nota)
    movie_mario.techinal_sheets()
    
#Modificando a variavel
Movie.platform = "OneBitCode Pro"
#plataforma é uma caracteristica comum a todos os objetos que foram instanciados.
movie_mario.techinal_sheets()