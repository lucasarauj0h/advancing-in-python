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

# 2 - solicitando dados do usuário

name = input('nome do filme: \n')
year = int(input('ano de lançamento: \n'))
score = float(input('nota do filme: \n'))

# 3 - inserindo os dados:
# - INSERT : para inserir

# - INTO : [para inserir] - EM (neste caso, tabela movies, e os parametros da tabela)
# - VALUES (?, ?, ?) : inserindo de modo dinamico, após a """ é passado uma tupla com
# as variaveis que serão adicionadas/inseridas, na mesma ordem!

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score))


# 4 - fechando a conexão

connection.commit()
print("tabela criada com sucesso")
#fechando a conexão
connection.close()