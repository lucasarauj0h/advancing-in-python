
'''
## Cadastro de Viagem

Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:

1. Usuário deve informar o seu nome para cadastrar uma viagem.
2. Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.
3. Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no destino 
específico foi feito com sucesso.
'''

class Client():
    def __init__(self, name):
        self._name = name

    

class Trips(Client):
        def __init__(self, name, trip=None):
            super().__init__(name)
            self.trip = trip
            
        def options(self):
            print("Opções de viagems disponiveis: ")
            trips = ["Milão", "Africa do Sul", "Arabia Saudita", "Sudão", "Moçambique"]
            for i in range(len(trips)):
                print(f'{i}. {trips[i]}')
            option = int(input("Escolha uma opção: "))
            for i in range(len(trips)):
                self.trip = trips[option]
                
        def __str__(self):
            return f'Cliente embarcará no vôo para {self.trip}'
        
lucas = Trips("Lucas")
lucas.options()
print(lucas)