from entities.trips import Trip

trip0 = Trip("Moçambique")
trip1 = Trip("Nova Guiné")
trip2 = Trip("Sudão do Sul")
trip3 = Trip("Nigéria")
trip4 = Trip("Etiópia")

traveler = input("Qual o seu nome? ")


list_trip = [trip0,trip1,trip2,trip3,trip4]
print(f'Destinos disponiveis: ')
list_trip = [trip0,trip1,trip2,trip3,trip4]
for i in range(len(list(list_trip))):
    string = str(list_trip[i].destiny)
    print(f'[{i}]. {str(string)}')

choice = int(input("Digite uma opção "))

for option in list_trip:
    if choice >= 5:
        print("Está opção não está disponivel no momento")
        break
    if choice <= 4:
        print(f'{traveler} sua viagem para {list_trip[choice].destiny} está marcada')
        break
    
        