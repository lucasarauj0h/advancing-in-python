class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity   
                    
    def totalValueStock(self):
        return self.quantity*self.price
    def addProducts(self,qntd):
        self.quantity += qntd    
        print(f'Foram adicionados {qntd} {self.name} ao estoque')
    def removeProducts(self, qntd):
        self.quantity -= qntd
        print(f'Foram retirados {qntd} {self.name} ao estoque')
    