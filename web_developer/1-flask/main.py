'''
https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=

https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=

https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=

key: cad33cb92ca0fa9baf86ee9240dc74d4
'''

from flask import Flask, render_template, request
from projeto.lista_filmes import resultado_filmes
from flask_sqlalchemy import SQLAlchemy
from livro import livro

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)

 
# rota: localhost:5000/
conteudos = []
registros = []
@app.route('/', methods=["GET", "POST"])
def principal():
    # Aula 9: trazendo dados do clique
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
    conteudo1 = 'Manipulação de Dados'
    conteudo2 = 'Herança e Templates'
    conteudo3 = 'Integração de APIs'
    conteudo4 = 'Banco de Dados'
    return render_template(
        'index.html',
        conteudo1=conteudo1,
        conteudo2=conteudo2,
        conteudo3=conteudo3,
        conteudo4=conteudo4,
        conteudos = conteudos
    )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/diario', methods=['GET','POST'])
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            registros.append(
                {
                'aluno': aluno,
                'nota': nota
                }
            )
    return render_template('sobre.html',
                           registros = registros)

@app.route('/filmes/<propriedade>')
def lista_filmes(propriedade):
    return render_template(
        "filmes.html", 
        filmes=resultado_filmes(propriedade)
    )
    
@app.route('/livros')
def lista_livros():
    return render_template(
        'livros.html',
        livros=livro.query.all()
        )    