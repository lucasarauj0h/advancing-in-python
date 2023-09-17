import json 
from itertools import combinations, permutations, product

def add_json():
    pessoa = {
        'nome': 'Luiz Otávio 2',
        'sobrenome': 'Miranda',
        'enderecos': [
            {'rua': 'R1', 'numero': 32},
            {'rua': 'R2', 'numero': 55},
        ],
        'altura': 1.8,
        'numeros_preferidos': (2, 4, 6, 8, 10),
        'dev': True,
        'nada': None,
    }
    #muito utilizado para armazenar dados
    with open('aprendendo_json.json', 'w+', encoding='utf8') as arquivo:
        json.dump(
                pessoa,  #atribuimos a variavel pessoa dentro do arquivo #pessoa -> dados
                arquivo, # -> arquivo do as arquivo, pois abri a pasta chamando-o de arquivo
                ensure_ascii=False, #formantando sem problemas com acentos e/outros  
                indent=2 #formatando em uma identação mais aceitavel
                ) 

def print_iter(iterator):
    print(*list(iterator), sep='\n')

with open('aprendendo_json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
    # print_iter(pessoa)
    
