class Employee():
    def __init__(self, name, gross_salary, tax):
        self._name = name
        self.__gross_salary = gross_salary
        self._tax = tax
       
    def netSalary(self):
        return (self.__gross_salary - self._tax)
    
    def gross_salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Nome deve ser uma string")
        self.__gross_salary *= (1+value/100)        

empregado = Employee("Lucas", 6000, 1000)

print(empregado.netSalary())
empregado.gross_salary(50)

print(empregado.netSalary())