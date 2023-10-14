from ConnectionPostgreSQL import connection, read_bd

cursor_obj = connection.cursor()

print(cursor_obj)

sql = """
    DELETE FROM game
    WHERE id = %s
"""

cursor_obj.execute(sql, (9,))
cursor_obj.execute(sql, (10,))
connection.commit()
print("Dado removido da Base de Dados com sucesso!")
print()
read_bd()