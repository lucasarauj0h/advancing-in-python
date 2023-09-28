"""
1 - O método estático não possui o parâmetro self.
2 - O método de classe pode acessar mas não pode modificar o estado da classe 
3 - Usamos o decorator @staticmethod em python para criar um método estático
""" 

class Language:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    @staticmethod #@ são decorators, e são muito usados em python. 
    def course_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Modulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com python":
            courses = ["Automação de tarefas", "Web Scraping", "Assistente Virtual em Python"]
        else:
            courses = "A definir."
            
        return courses
        
print(Language.course_trail("Python Fundamentos"))
print(Language.course_trail("Análise de dados"))
print(Language.course_trail("Automação com python"))

#acessamos items dentro da classe mas não mudamos nada, nem instanciamos ou 
#alteramos qualquer coisa presente dentro da classe.