class Phone():
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
        
    def __str__(self):
        return f'{self._brand}{self._model_name}'
    
    @staticmethod
    def make_a_call(phone_num):
        print(f'Ligando para: {phone_num}')
        
class SmarthPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) #lembrar dos parenteses ao usar o super
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        
        
moto = Phone('Moto', "G7", 1250)
print(moto)
moto.make_a_call(934241563)
print(vars(moto))

iPhone = SmarthPhone("Iphone", "Xs", 5500, "6gb", "128gb", "48MP")
print(iPhone)
print(vars(iPhone))