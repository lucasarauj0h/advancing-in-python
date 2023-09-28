class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')
        
    #metodo para buscar os dados (get = me dê)
    def get_salary(self):
        return self.__salary
    
    #metodo para alterar os dados (set = setar, mudar)
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = Employee("Fulano", 8800)
ciclano = Employee("Ciclado", 5500)

fulano.show()
ciclano.show()
fulano.__salary = (85456000000)
try:
    fulano.__salary = (8000000) #não posso deixar o salario publico, porque se não
    #qualquer um poderia alterar esses dados. Para evitar esse uso, colocamos
    # __ (duas vezes underline) para tornar esse atributo privado
except:
    print("Não foi possivel usar o codigo acima")
fulano.show()
# fulano.set_salary(4540504)
fulano.show()
#com o encapsulamento, só é possivel alterar um objeto atraves de um metodo 