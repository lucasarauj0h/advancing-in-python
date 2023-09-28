#o class method é um methodo que pode ser chamado antes mesmo de ser instanciado
#intanciado e quando atribuimos a class a uma variavel, exemplo:
#movie_mario = Movie("Mario", 0, 0)
#os metodos só podem ser chamado com uma instancia,
#os class method não precisam ser instanciados.

'''
1- o metodo de classe utiliza o parametro referente a classe
2- o metodo de classe pode acessar ou modificar o estado da classe
3- usamos o decorator @classmethod para criar um metodo de classe
'''

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        
        return cls(name, int(price))
    
wiiU = Console.from_text("Meu video game é WiiU e o preço é 1000 reais")
xbox = Console.from_text("Meu video game é Xbox e o preço é 2500 reais")
print(wiiU.__dict__)
print(xbox.__dict__)