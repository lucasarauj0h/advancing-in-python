from pymongo import MongoClient
from pprint import pprint

# Conectando-se ao mongo db
client = MongoClient()

# Conectando-se ao database "obcblog" a partir da conexão com o obj "client"
mydb = client.obcblog

# Conectando-se ao database com nome 'posts'
mycolection = mydb.posts

# Retorna o primeiro documento encontrado
result = mycolection.find_one()
pprint(result)
pprint("-" * 50)

# Retorna todos os documento encontrado
result = mycolection.find()
for r in result:
    pprint(r)
