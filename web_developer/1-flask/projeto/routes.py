from projeto import app, db
from flask import render_template, request, redirect, url_for
from projeto.lista_filmes import resultado_filmes
from projeto.livro import livro

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
    page = request.args.get('page', 1, type=int)
    per_page = 5
    todos_livros = livro.query.paginate(
        page=page, 
        per_page=per_page
        )
    
    return render_template(
        'livros.html',
        livros=todos_livros
        )    
    
@app.route('/add_livro', methods=['GET','POST'])
def adiciona_livro():

    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')
    
    if request.method == 'POST':
        livro_add = livro(
            nome,
            descricao,
            valor
        )
        db.session.add(livro_add)
        db.session.commit()
        return redirect(url_for('lista_livros'))
    return render_template("novo_livro.html")

@app.route('/<int:id>/atualiza_livro', methods=['GET','POST'])
def atualiza_livro(id):
    # quando eu uso <form action="{{url_for('adiciona_livro', id=livro.id )}}" method="POST">
    # o url_for('[]') indica a função de rota que é chamada, e o parametro indica o parametro dessa função 
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = request.form['valor']
    
        livro.query.filter_by(id=id).update(
            {
                "nome": nome,
                "descricao": descricao,
                "valor": valor
            }
        )
        db.session.commit()
        return redirect(url_for('lista_livros'))
    # SELECT * FROM livro WHERE id = []
    livro_bd = livro.query.filter_by(id=id).first()
    return render_template(
        'atualiza_livro.html',
        livro = livro_bd
    )
    
@app.route('/<int:id>/remove_livro')
def remove_livro(id):
    livro_bd = livro.query.filter_by(id=id).first()
    db.session.delete(livro_bd)
    db.session.commit()
    return redirect(url_for('lista_livros'))