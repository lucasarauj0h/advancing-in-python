from entities import Product_Archive

pneu = Product_Archive.Product("Pneu", 45, 10)
print(pneu.totalValueStock())
pneu.addProducts(10)
print(pneu.totalValueStock())
pneu.removeProducts(15)
print(pneu.totalValueStock())
