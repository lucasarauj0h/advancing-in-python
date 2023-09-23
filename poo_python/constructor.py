class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLauch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
        
try:
    movie = Movie() #usando o metodo construtor, eu quero dizer que passarei os atributos
    #assim q eu instanciar a classe
    print(movie)
    
except:
    print()
movie = Movie("Super Mario Broos", 2023, False, 5.0, 130)
movie_avatar = Movie("Avatar", 2023, False, 4.3, 200)
print(f'Filme: {movie.name}\nNota: {movie.note}')
print(f'Filme: {movie_avatar.name}\nNota: {movie_avatar.note}')

        