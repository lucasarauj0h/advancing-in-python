from flask import Flask, render_template, request

app = Flask(__name__)

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
