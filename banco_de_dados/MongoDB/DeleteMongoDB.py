from pymongo import MongoClient
from pprint import pprint

# Conectando-se ao mongo db
client = MongoClient()

# Conectando-se ao database "obcblog" a partir da conexão com o obj "client"
mydb = client.obcblog

# Conectando-se ao database com nome 'posts'
mycolection = mydb.posts

# Criando um post com o dicionário, por ser o mais semelhante a linguagem json.
post1 = {
    "title": "FastAPI",
    "category": "Backend",
    # Colocando um agregado dentro de outro 
    "author": {
        "name": "Letiii",
        "email": "souzaxlavel@gmail.com"
    }
}

mycolection.insert_one(post1)
print("Documentos incluído com sucesso.")

# Orgazinando as variaveis, com os parametros que serão deletados 
myquery = { "title": "FastAPI" }

x = mycolection.delete_one(myquery)

print(f'{x.deleted_count} documentos excluídos')

for r in mycolection.find():
    pprint(r)

