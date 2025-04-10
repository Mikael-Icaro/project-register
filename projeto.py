from flask import Flask, render_template, request, redirect #importando biblioteca
#a linha abaixo importa o sqlalchemy para o projeto
from flask_sqlalchemy import SQLAlchemy
  
# a linha a baixo cria a variavel de aplicação 
app = Flask(__name__)

# a linha abaixo é a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'aluno',
        senha = 'toor',
        servidor = 'localhost',
        database = 'prj_cadastro'
    )

# a linha abaixo instancia o banco de dados
db = SQLAlchemy(app)

class Aluno(db.Model):
    ra_aluno = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome_alunno = db.Column(db.String(80), nullable = False)
    idade_aluno = db.Column(db.Integer, nullable = True)
    email_aluno = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "<Name %r>"% self.name



# a linha a baixo cria uma rota

@app.route('/hello')
def ola ():
    return "<h2>Iniciando projeto com flask</h2>"

@app.route('/lista')
def lista_alunos():

    # a linha abaixo cria uma lista de alunos
    
    lista_alunos_cadastrados = Aluno.query.order_by(Aluno.ra_aluno).all()
    return render_template("lista.html", titulo = "Unifecaf", alunos = lista_alunos_cadastrados) 


# a partir daqui tatamos a tela "cadastrar.html"
@app.route('/cadastrar')
def cadastrar_aluno():
    return render_template('cadastrar.html')

@app.route('/add_aluno', methods=['POST'])
def adicionar_aluno():

    # as variaveis abaixo vão receber os dados
    # preenchidos na pagina cadastrar.html
    ra_recebido = request.form['txtRA']
    nome_recebido = request.form['txtNome']
    idade_recebida = request.form['txtIdade']
    email_recebido = request.form['txtEmail']

    # a linha abaixo instancia um novo aluno
    novo_aluno = Aluno(ra_aluno = ra_recebido, nome_alunno = nome_recebido, 
                       idade_aluno = idade_recebida, email_aluno = email_recebido)
    # a linha abaixo adiciona o novo aluno na lista
    #lista_alunos_cadastrados.append(novo_aluno)
    return redirect('/lista')
    # a linha abaixo redireciona para a pagina lista.html


# a linha a baixo deve ser a ultima linha do projeto
app.run()

