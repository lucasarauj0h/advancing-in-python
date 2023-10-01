class AccountBank:
    TAX = 5
    
    def __init__(self, id, name, initialDeposit):
        self.__id = id
        self._name = name
        self.__balance = initialDeposit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("O nome deve ser uma string")

    @property
    def balance(self):
        return self.__balance 

    def withdraw(self, value):
        if (self.__balance + AccountBank.TAX) >= value:
            self.__balance -= (value + AccountBank.TAX)
        else:
            print("Saldo indisponível")

    def deposit(self, value):
        if value >= 0:
            self.__balance += value
        else:
            raise ValueError("O valor do depósito deve ser não negativo")

    @property
    def id(self):
        return self.__id

# Exemplo de uso
account = AccountBank(1, "João", 1000)
account.id = 45
print(vars(account))