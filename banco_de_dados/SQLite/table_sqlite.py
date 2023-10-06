import sqlite3

connection = sqlite3.connect('banco_de_dados/SQLite/title.db')

# criando uma tabela em sqlite
# para manipular os dados (DMl) de um banco de dados, é preciso criar um cursor

'''cursos é um iterador que permite nagevar e manipular os registros de um BD'''

cursor = connection.cursor()

# criando a tabela de fato. 

#Descrição:
# - INTEGER : definindo um numero inteiro
# - NOT NULL : "Não pode ser vazio"
# - PRIMARY KEY : Chave Primaria, ou ainda, única para cada um 
# - AUTOINCREMENT : Adicionar o valor automaticamente (começando pelo 1)
# - TEXT : do tipo texto
# - REAL : do tipo numeros reais


cursor.execute("""
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        YEAR INTEGER NOT NULL,
        score REAL NOT NULL
    ); 
               """)

# 4 - fechando a conexão

connection.commit()
print("tabela criada com sucesso")

#fechando a conexão

connection.close()