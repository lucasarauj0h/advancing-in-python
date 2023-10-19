class Animal():
    def __init__(self, size, color):
        self.size = size
        self.color = color
        
    def eat():
        print("Hora de comer!")
        
class Horse(Animal):
    def __init__(self, race):
        Animal.__init__(self)
        self.race = race
        
    def escape():
        print("O cavalo escapou!") #pr
        
class Lion(Animal):
    
    def __init__(self,race):
        Animal.__init__(self)
        self.race = race
        
    def hunt():
        print("O leão está cassando!")
        

fluffy = Lion("Cabeludo", "1,70m", "Blue") 

