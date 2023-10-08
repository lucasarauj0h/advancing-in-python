from connection_ORM_postgreSQL import Base, engine, session
from User import User
from Post import Post

# cria as tabelas
Base.metadata.create_all(engine)

# Função para exibir o menu de opções

def show_menu():
    print("Menu de opções:\n1. Adicionar Usuário\n2. Adicionar Post\n3. Consultar \
Usuários e Posts\n4. Sair")
    
# Função para adicionar usuário

def add_user():
    print("Adicionar novo usuário")
    name = input("Digite seu nome:\n")
    email = input("Digite seu e-mail:\n")
    #construindo nossa classe de nome e usuário (User)
    user = User(name, email)
    #adicionando a classe atribuida ao obj user, no BD (session.add(...))
    #como se fosse o insert do SQL, porem resumido e em uma classe.
    session.add(user)
    session.commit()
    print("Usuário adicionado com sucesso.")
    
# Função para adicionar post

def add_post():
    print('Adicionar novo post:')
    title = input("Digite um título:\n")
    content = input("Conteudo:\n")
    author_id = input("Id do Autor:\n")
    user = session.query(User).filter_by(id=author_id).first()
    #o user vai receber o nome, assim que ele encontrar o ID informado
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
    else:
        print("Usuário não encontrado.")
        
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f'Users: {user.name}, Email: {user.email}')
        for post in user.posts:
            print(f"Post: {post.title}\n Content:{post.content}")