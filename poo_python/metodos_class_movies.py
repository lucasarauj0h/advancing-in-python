class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLauch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self):
        return f'Filme: {self.name}'
    
    def techinal_sheet(self):
        print("Dados do filme: ")
        print(f'Filme: {self.name}')
        print(f'Ano de lançamento: {self.yearLauch}')
        print(f'Está em algum plano?: {self.includePlan}')
        print(f'Nota do filme: {self.note}')
        print(f'Duração do filme: {self.durationMinutes}')
        
movie_mario = Movie("Super Mario Broos", 2023, False, 5.0, 130)
movie_avatar = Movie("Avatar", 2023, False, 4.3, 200)

movie_mario.techinal_sheet()
print("-"*50)
movie_avatar.techinal_sheet()