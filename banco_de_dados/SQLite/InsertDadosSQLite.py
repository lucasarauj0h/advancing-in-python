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

# 3 - Inserindo Dados
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Super Mario Bros', 2023, 9.5)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Avatar', 2023, 10.0)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Velozes & Furiosos', 2023, 8.5)
""")    

# 4 - Gravando Dados no BD
connection.commit()
print('Dados inseridos com sucesso.')

# 5 - Fechando conexão
connection.close()