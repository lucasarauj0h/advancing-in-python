from connection_ORM_postgreSQL import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# nossa classe user vai estar utilizando ORM
# os atributos não serão apenas atributos da classe, mas colunas da BD
class User(Base):
    __tablename__ = 'users' #definindo o nome da tabela, utilizando como herança a classe
    # base. essa classe permite que criemos modelos de tabelas 
    
    id = Column(Integer, primary_key=True) 
    name = Column(String)
    email = Column(String)
    posts = relationship('Post', back_populates='author') #essa linha define um
    #relacionamento entre o posts do user e a tabela Post, com a coluna "author"
    # é bidirecional, o q significa q um usuario pode estar relacionado a 
    # varios posts, um post tmb estará relacionado a um usuario

    
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        