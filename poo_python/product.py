class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def priceTag(self):
        return f'{self.name} R$ {self.price}'

class ImportedProduct(Product):
    
    def __init__(self, name, price, customsFee):
        super().__init__(name, price)
        self.customsFee = customsFee
        
    def priceTag(self):
        totalPrice = self.price + self.customsFee
        return f'{self.name} R$ {totalPrice} (Customs fee: {self.customsFee})'
    
class UsedProduct(Product):
    
    def __init__(self, name, price, manufactureDate):
        super().__init__(name, price)
        self.manufactureDate = manufactureDate
        
    def priceTag(self):
        return f'{self.name} (used) R$ {self.price} (manufacture date: {self.manufactureDate})'
    

n = int(input("Quantos produtos deseja adicionar?"))
products = []
for i in range(n):
    option = input('Common, used or imported (c/u/i)\n')
    name = input("Name: ")
    price = float(input("Price: "))
    if option == 'i':
        tax = float(input("Customs fee: "))
        products.append(ImportedProduct(name, price, tax))
    elif option == 'u':
        manufacture_date = input("Manufacture date: (DD/MM/AAAA) - ")
        products.append(UsedProduct(name,price,manufacture_date))
    elif option == 'c':
        products.append(Product(name, price))
    else:
        print("Opção escolhida inválida.")
   
print('PRICE TAGS - ')     
for i in range(n):
    print(products[i].priceTag())
    