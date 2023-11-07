from pymongo import MongoClient

# Conectando-se ao mongo db
client = MongoClient()

# Conectando-se ao database "obcblog" a partir da conexão com o obj "client"
mydb = client.obcblog

# Conectando-se ao database com nome 'posts'
mycolection = mydb.posts

# Orgazinando as variaveis, com os parametros que serão atualizados 
myquery = { "category": "Backend" }
newvalues = {"$set": {"category": "Data Analysis"}}

# Realizando o update do *PRIMEIRO dos que contenha na parte "category" o dado "Backend"
mycolection.update_one(myquery, newvalues)

# Realizando o update de *TODOS os dados contenha na parte "category" o dado "Backend"
mycolection.update_many(myquery, newvalues)

# Retorna todos os documento encontrado
for r in mycolection.find():
    print(r)