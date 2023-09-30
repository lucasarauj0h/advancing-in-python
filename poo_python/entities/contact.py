'''
## Agenda de Contatos

Desenvolva uma agenda de contatos utilizando Programação Orientada a Objetos. O programa 
deve seguir as especificidades:

1. Ter uma classe Contact contendo os atributos: name, phone e email
2. Ter uma classe ContactBook contendo quatro métodos:
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para buscar contatos.
    4. Um método para remover contatos.
3. Criar um arquivo principal para a aplicação que deve instanciar as duas classes
criadas anteriormente e desenvolver e chamar cada um dos métodos desenvolvidos de 
acordo com a opção escolhida.
'''

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f'Nome {self.name}\nPhone: {self.phone}\nEmail: {self.email}'
