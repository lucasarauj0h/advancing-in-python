from connection_postgreSQL import connection

cursor_obj = connection.cursor()

sql = """
    UPDATE game 
    SET score = %s
    WHERE id = %s
"""
cursor_obj.execute(sql, (20.5, 4))
connection.commit()
print("Atualização realizada com sucesso")

print(cursor_obj)