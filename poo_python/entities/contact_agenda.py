class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def remove_contact(self, contact):
        self.contacts.remove(contact)
        
        
    def display_contact(self):
        if not self.contacts: #se não tivermos contatos para exibir
            print("Não há contatos a mostrar")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
        print("Contato não encontrado.")