from projeto import db

class livro(db.Model):
    # Criando uma coluna chamada ID, definindo o seu type e se é key primaria
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Integer)
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor 