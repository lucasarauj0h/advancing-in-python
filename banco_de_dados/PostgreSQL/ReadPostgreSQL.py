from ConnectionPostgreSQL import connection, read_bd

cursor_obj = connection.cursor()

print(cursor_obj)

# SELECT : 'selecione [*] - (todas) colunas 
# FROM : nesse contexto, selecione * todas colunas FROM [DE] ['TABELA'] game
cursor_obj.execute('''
    SELECT * FROM game
                    ''')

# fetchall : todos os registros salvos no objeto cursos_obj

result = cursor_obj.fetchall()

print(result)