from connection_postgreSQL import connection

cursor_obj = connection.cursor()

# inserindo 2 dados de forma simultanea no BD

games = [
    ('Star Wars Survivor', 2023, 9.0),
    ('Luigis Mansion 3', 2019, 5.7)
]

for game in games:
    print(game)
    cursor_obj.execute("""
            INSERT INTO game (name, year, score)
            VALUES (%s, %s, %s)
                       """, game)
    
# enviando as atualizações e fechando a abertura.
# temos que fechar o cursos e commitar aonde abrimos (connection.cursor())
# o objeto "cursor_obj" serve apenas para nos auxiliar na manipulação indireta. 

connection.commit()
print("Dados inserido com sucesso")
connection.close()