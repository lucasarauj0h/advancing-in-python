#alterações em classes, com objetos privados recomenda-se ao inves do uso de 
#getter/setter, usa-se os decorators property

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    #quando usar o property, deixar os objetos protegidos.
    @property #metodo getter
    def name(self):
        return self._name
    
    @name.setter #metodo setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string")
        self._name = value
            
            

pessoa = Person( "Lucas + Leticia <3" , "20 e 018")
print(vars(pessoa))
print(pessoa.name)
pessoa.name = "Lucas"
print(pessoa.name)