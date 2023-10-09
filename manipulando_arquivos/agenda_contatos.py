'''
## Agenda de Contatos

Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve 
seguir as especificidades:

1. Criar o arquivo Agenda contendo quatro métodos:
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para remover contatos.
2. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar 
cada um dos métodos desenvolvidos de acordo com a opção escolhida.
'''
import csv

contatos = []
t = True
        
with open("contact.csv", 'r', encoding='utf-8') as file:
    for line in file:
        name, number = line.rstrip().split(',')
        contact = {}
        contact["name"] = name
        contact["number"] = number
        contatos.append(contact)       
        

def addContact(contatos, name, number):
    contatos.append({"name": name, "number": number})
    return contatos

def removeContact(contatos, name):
    count = 0
    for i in contatos:
        for key, value in i.items():
            print(key, value)
            if key == "name":
                if value == name:
                    a = contatos.pop(count)
                    name, number = a.values()
                    print(f"nome: {name}\n number: {number}\nContato removido com sucesso")
                else:
                    print('Nome invalido!')
                count += 1
                
def listContact(contatos):
    c = 0
    for i in contatos:
        name, number = i.values()
        if name == "name":
            ...
        else: 
            c = 1
            print(f"Nome: {name} - Numero: {number}")
    if c != 1:
        print(f'Lista de contatos vazia, adicione algum contato.')


while t:
    print('Escolha uma opção: \n')
    choice = input("1. Adicionar contato\n2. Listar contatos\n3. Remover contato\n4. Sair\n")
    if choice == "1":
        name = input("Qual o nome: \n")
        number = input("Qual o numero? \n")
        addContact(contatos, name, number)
    elif choice == "2":
        print("*"*50)
        listContact(contatos)
        print("*"*50)
    elif choice == "3":
        remove = input("Qual contato deseja remover: \n")
        removeContact(contatos, remove)
    elif choice == "4":
        with open("contact.csv", 'w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            for i in contatos:
                name, number = i.values()                           
                print(i, name, number)
                writer.writerow([name, number])

        t = False
        print("Agenda salva em contact.csv")
    else:
        print("Opção inválida!")
        