class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity   
                    
        def totalValueStock():
            return quantity*price
        def addProducts(qntd):
            quantity += qntd    
        def removeProducts(qntd):
            quantity -= qntd
    