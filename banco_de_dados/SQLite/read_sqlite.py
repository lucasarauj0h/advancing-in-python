import sqlite3

connection = sqlite3.connect('banco_de_dados/SQLite/title.db')

# criando uma tabela em sqlite
# para manipular os dados (DMl) de um banco de dados, é preciso criar um cursor

'''cursos é um iterador que permite nagevar e manipular os registros de um BD'''

cursor = connection.cursor()

# lendo dados da tabela 
# SELECT : seleciome as variaveis (...)
# FROM movies : da tabela movies
# * : faz referencia a todas as colunas da base de dados
data = cursor.execute("""
        SELECT * FROM movies
                      """)
print(data.fetchall())

# iterando os dados

for i in cursor.execute("SELECT * FROM movies"):
    id, name, year, score = i
    print(f"ID: {id}\nname: {name}\nYear: {year}\nScore: {score}")
# fetchall : pegue todos os dados dessa instrução e envie via print
#resultara em uma lista de tuplas, e cada tuplas represnta um registro na base de dados

# 4 - ordenando os dados pelo score

# ORDER BY : ordene por [coluna]; por padrão ele ordena no menor ao maior
# desc - para inverter a ordenação, do maior para o menor
for i in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    id, name, year, score = i
    print(f"ID: {id}\nname: {name}\nYear: {year}\nScore: {score}")

# 5 - Fechando conexão
connection.close()