from pymongo import MongoClient

# Conectando-se ao mongo db
client = MongoClient()

# Criando um database a partir da conexão com o obj "client"
mydb = client.obcblog

# Criando uma coleção no database com nome 'posts'
mycolection = mydb.posts

# Criando um post com o dicionário, por ser o mais semelhante a linguagem json.
post1 = {
    "title": "StreamLit",
    "category": "Data Analysis",
    # Colocando um agregado dentro de outro 
    "author": {
        "name": "Lucas",
        "email": "souza.a@gmail.com"
    }
    
}

post1 = {
    "title": "FastAPI",
    "category": "Backend",
    # Colocando um agregado dentro de outro 
    "author": {
        "name": "Letiii",
        "email": "souzaxlavel@gmail.com"
    }
    
}

# Inserindo o post no database criado.
result = mycolection.insert_one(post1)
print("Documentos incluído com sucesso.")
print(client)