from entities.contact import Contact
from entities.contact_agenda import ContactBook

contato_agenda = ContactBook()

while True:
    print("\n ---- opções agenda de contat ----")
    print(
        "\t1. Adicionar contato\n\
        2. Remover contato\n\
        3. Listar contato\n\
        4. Buscar contato\n\
        5. Sair\
        \n"
        )
    
    choice = input("Escolha uma das opções: \n")
    
    if choice == "1":
        name = input("Digite o nome: \n")
        phone = input("Digite o telefone: \n")
        email = input("Digite o email: \n")
    
        contact = Contact(name,phone,email)
        contato_agenda.add_contact(contact)
        print("contato adicionado com sucesso.")
    
    elif choice == "2":
        name = input("Informe o nome do contato para remover: \n")
        contact = contato_agenda.search_contact(name)
        if contact:
            contato_agenda.remove_contact(contact)
            print("Contato removido com sucesso.")
            
    elif choice == "3":
        contato_agenda .display_contact()
        
    elif choice == "4":
        name = input("Informe o nome do contato para buscar: \n")
        contact = contato_agenda.search_contact(name)
        
    elif choice == "5":
        break
    else:
        print("Opção inválida.")        
        
            
    