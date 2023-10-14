import requests

from pymongo import MongoClient
from pprint import pprint

# Conectando-se ao mongo db
client = MongoClient()

# Conectando-se ao database "obcblog" a partir da conexão com o obj "client"
db = client['nobel']

# Importando os dados em documentos
for collection_name in ["prizes", "laureates"]:
    response = requests.get(
        f"https://api.nobelprize.org/v1/{collection_name[:-1]}.json")
    
    documents = response.json()[collection_name]                   
    db[collection_name].insert_many(documents)   
    
# Acessando coleções / contagem de documentos na coleção
prizes = db['prizes']
laureates = db['laureates'] 

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})

print(len_prizes)
print(len_laureates)

