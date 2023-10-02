class Employee:
    def __init__(self, name, hours, valuePerHour):
        self.__name = name
        self.__hours = hours
        self.__valuePerHour = valuePerHour
    
    @property
    def name(self):
        return self.__name
    
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if isinstance(value, (int, float)):
            self.__hours = value
        else:
            raise ValueError("As horas devem do tipo int ou float")
        
    @property
    def valuePerHour(self):
        return self.__valuePerHour
    
    @valuePerHour.setter
    def valuePerHour(self, value):
        if isinstance(value, (int, float)):
            self.valuePerHour = value
        else:
            raise ValueError("As horas devem do tipo int ou float")
        
    def payment(self):
        return self.__valuePerHour * self.__hours
    
    
class OutsourcedEmployee(Employee):
    
    def __init__(self, name, hours, valuePerHour, additionalCharge):
        super().__init__(name, hours, valuePerHour)
        self.__additionalCharge = additionalCharge
        
    @property
    def additionalCharge(self):
        return self.__additionalCharge
    
    @additionalCharge.setter
    def additionalCharge(self, value):
        if isinstance(value, (int, float)):
            self.__additionalCharge = value
        
    def payment(self):
        print(super().payment())
        return super().payment() + self.__additionalCharge
    
funcionario = []
n = int(input("Quantos funcionários deseja adicionar\n"))
for i in range(n):
    name = input("Qual o nome\n")
    hours = int(input("Quantas horas de trabalho\n"))
    valuePerHour = float(input("Qual o valor por hora de trabalho\n"))
    option = input("Empregado terceirado? (y/n)\n ")
    if option == 'y':
        additional = float(input("Pagamento adicional\n"))
        funcionario.append(OutsourcedEmployee(name, hours, valuePerHour, additional))
    else:
        funcionario.append(Employee(name, hours, valuePerHour))
        
print("Payments:\n")
for i in range(n):
    print(f'Funcionário: {funcionario[i].name}', funcionario[i].payment())