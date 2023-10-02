class Animal():
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
class Fish(Animal):
    race = ''
    
class Parrots(Animal):
    color = ''
    
class Zoo():
    def __init__(self):
        self.animals_dict = {} #criando animal_dict como dicionário
        
    def add_animal(self, animal):
        self.animals_dict [animal.name] = animal.category #adiciono o nome do animal
        #atribuido a uma categoria
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f'no nosso zoologico temos {result} quantidade de {category}'
    
zoo = Zoo()

peixe = Fish("Nemo", "mamifero") #criando a subclasse, passando parametro pra classe-pai
#nome, e categoria
print(vars(peixe))

        