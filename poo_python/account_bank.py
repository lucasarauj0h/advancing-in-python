class AccountBank():
    TAX = 5
    
    def __init__(self, id, name, initialDeposit=0):
        self.__id = id
        self._name = name
        self.__balance = initialDeposit
          
    def __str__(self):
        return f'Account {self.__id}, Holder: {self._name}, Balance: R$ {self.__balance}'
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string")
        self._name = value
    
    @property
    def balance(self):
        return self.__balance
        
    def withdraw(self, value):        
        if (self.__balance) >= (value+AccountBank.TAX):
            self.__balance -= (value + AccountBank.TAX)
            print(f'Você realizou o saque de {value} + taxa {AccountBank.TAX} \
                \nSaldo atual: {self.__balance}')
        else: 
            print("Saldo indísponivel")
    
    def deposit(self, value):
        if value >= 0:
            self.__balance = value
            print(f'Você realizou o deposito de {value}\nSaldo atual: {self.__balance}')
            

account_Joao = AccountBank(1, "João")
account = AccountBank(2, "Lucas", 5000)
account_Ana = AccountBank(3, "Anna", 7000)

print(account)
account.withdraw(1)
account.name = "Ana"
print(account)
print(account_Joao)