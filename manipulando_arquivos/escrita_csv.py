import csv

# name = input("Informe o nome da linguagem que deseja aprender\n")
# category = input("Qual a categoria a linguagem se encaixa\n")

name = ["japa", "texto", "futebol", "bola"]
category = ['1', '2', '3', '4']

lista = []

    

with open("contact.csv", 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    for i in range(len(name)):
        print(name[i], category[i])
        writer.writerow([name[i], category[i]])
    
