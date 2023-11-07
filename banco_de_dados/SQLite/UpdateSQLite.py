#criar um banco de dados "titulos" contendo nome, ano de lançamento, duração de um filme

import sqlite3

# criando o banco de dados

connection = sqlite3.connect("banco_de_dados/SQLite/title.db") #criando uma base de dados com o nome "title"

# criando uma tabela em sqlite
# para manipular os dados (DMl) de um banco de dados, é preciso criar um cursor

'''cursos é um iterador que permite nagevar e manipular os registros de um BD'''

cursor = connection.cursor()

# ao atualizar dados, é necessário definir uma condição, no contexto das base de dados
# é importante sempre atualziar a partir da condição da base de dados a chave primaria
# (clausula WHERE)

# 3 - solicitando dados do usuário

id = int(input("Informe o ID do filme que deseja atualizar\n"))
name = input("Novo nome do filme:\n")

# função WHERE, é o parametro condicional, onde passamos qual id devemos atualizar
# o nome; caso não exista nenhuma condição, será atualizado TODOS OS NOMES 
# (clausula WHERE)

cursor.execute("""
        UPDATE movies set name = ?
        WHERE id = ?
               """, (name, id))
# precisamos fazer um commit para que o BD se atualize
connection.commit()
print("Dados atualizados!")

# 5 - Fechando conexão
connection.close()