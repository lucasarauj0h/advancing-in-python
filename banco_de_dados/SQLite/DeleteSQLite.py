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

id = int(input("Informe o ID do filme que deseja remover\n"))


# DETELE : Remova
# FROM [tabela] : ['remova'] da tabela ['tabela']
# função WHERE, é o parametro condicional, onde passamos qual id devemos remover
# o nome; caso não exista nenhuma condição, será removido TODOS OS DADOS 
# (clausula WHERE)

cursor.execute("""
        DELETE FROM movies 
        WHERE id = ?
               """, (id,)) # CASO EU DEIXA APENAS ID, PYTHON IRA INTERPRETAR
# QUE ESTOU PASSANDO UMA STRING, USO A VIRGULA PARA MOSTRAR QUE E UMA TUPLA.
# precisamos fazer um commit para que o BD se atualize
connection.commit()
print("FILME REMOVIDO COM SUCESSO!")

# 5 - Fechando conexão
connection.close()