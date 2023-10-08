from connection_ORM_postgreSQL import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts" #definindo o nome da tabela como posts
    
    id = Column(Integer, primary_key=True) #criamos uma coluna chamado ID
    title = Column(String) # criamos uma coluna chamada titulo
    content = Column(String) #criamos uma coluna com o conteudo
    author_id = Column(Integer, ForeignKey('users.id')) #define uma coluna chamada 
    # author_id. essa coluna sera usada para armazenar o ID do autor do post.
    # a função ForeignKey estabele um relacionamento entre a coluna author_id e id
    # da tabela users. isto é, essa coluna é uma chave estrangeira que se refere
    # a resgistros da tabela users
    #essa coluna será usada para armazerar o id do autor do post 
    
    author = relationship('User', back_populates='posts') # define um relacionamento
    # entre a classe posts e a classe users no banco de dados. back_populates indica 
    #que a relação tambem sera definida na classe posts
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content 
        self.author = author