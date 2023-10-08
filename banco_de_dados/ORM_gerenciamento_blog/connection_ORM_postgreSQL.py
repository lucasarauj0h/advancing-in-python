from sqlalchemy import create_engine #importa a função 'create_engine' que é usada
# para criar uma conexão com o banco de dados.
from sqlalchemy.orm import sessionmaker # classe sessionmaker, usada para criar objetos
# de sessão do banco de dados, usada para interagir com o BD de forma mais conveniente
from sqlalchemy.ext.declarative import declarative_base # função declarative_base
#  que é usada para definir modelos de dados que representam tabelas do banco de dados.

# DATABASE_URI = 'postgresql://[user]:[password]@[localhost]/[database]'
user = 'postgres'
password = ''
host = 'localhost'
database = 'blog'

# essa variavel cria uma conexão com o BD postgreSQL 
DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

# Aqui, a função create_engine é usada para criar um objeto de mecanismo de conexão com o 
# banco de dados. Esse mecanismo é usado para se comunicar com o banco de dados e
# executar consultas.

engine = create_engine(DATABASE_URI)

# uma classe de fabrica sessão, usada para criar instancias de sessão que serão usadas
# para interagir com o BD 

Session = sessionmaker(bind = engine)

# abaixo, uma instancia de sessão usando a classe de fabrica 'Session'. Essa
# instancia sera usada para poder executar consultas e transasões no BD

session = Session()

# criando uma instancia chamada 'Base' para usar como base p/ definir modelos de dados
# (orm) (classes que representam tabelas do banco de dados) usando o SQLAlchemy.

Base = declarative_base()
'''
Em resumo, este código configura uma conexão com um banco de dados PostgreSQL usando o 
SQLAlchemy e cria uma classe de fábrica de sessão para trabalhar com o banco de dados. 
Isso é útil ao criar aplicativos que precisam se comunicar com bancos de dados 
PostgreSQL
'''