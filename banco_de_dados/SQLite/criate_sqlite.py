#criar um banco de dados "titulos" contendo nome, ano de lançamento, duração de um filme

import sqlite3

# criando o banco de dados

connection = sqlite3.connect("banco_de_dados/SQLite/title.db") #criando uma base de dados com o nome "title"

# verifica se houve alguma alteração na base de dados 

print(connection.total_changes)

