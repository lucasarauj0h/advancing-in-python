class Movie: #não posso extrair informação da classe
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

#como instanciar uma classe;
movie = Movie() #passei essa classe à uma variavel
#agora posso atribuir os metodos da classe a essa variavel
movie.name = "Super Mário Bross"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130
print("Dados do filme: ")
print(f'nome do filme: {movie.name}\nano de lançamento: {movie.yearLaunch}')

#como instanciar uma classe;
mario = Movie() #passei essa classe à uma variavel
#agora posso atribuir os metodos da classe a essa variavel
mario.name = "Super Mário Bross"
mario.yearLaunch = 2023
mario.includedPlan = False
mario.note = 5.0
mario.durationMinutes = 130
print("Dados do filme: ")
print(f'nome do filme: {mario.name}\nano de lançamento: {mario.yearLaunch}')

