from flask import Flask, render_template, request, redirect #importando biblioteca

class Aluno:
    def __init__(self, ra, nome, idade, email):
        self.ra_aluno = ra
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.email_aluno = email 


    # as 3 linhas instancia alunos
aluno01 = Aluno('1000', 'Daniel', '32', 
                    'daniel@pro.fecaf.com.br')
    
aluno02 = Aluno('1001', 'Matheus', '28',
                     'mathes.mat@fecaf.com', )
    
aluno03 = Aluno('1002', 'Angela Costa', '34',
                    'angela.costa@a.fecaf.com.br')
    
lista_alunos_cadastrados = [aluno01, aluno02, aluno03]

# a linha a baixo cria a variavel de aplicação 
app = Flask(__name__)

# a linha a baixo cria uma rota

@app.route('/hello')
def ola ():
    return "<h2>Iniciando projeto com flask</h2>"

@app.route('/lista')
def lista_alunos():

    # a linha abaixo cria uma lista de alunos
    

    return render_template("lista.html", titulo = "Unifecaf", alunos = lista_alunos_cadastrados) 


# a partir daqui tatamos a tela "cadastrar.html"
@app.route('/cadastrar')
def cadastrar_aluno():
    return render_template('cadastrar.html')

@app.route('/add_aluno', methods=['POST',])
def adicionar_aluno():

    # as variaveis abaixo vão receber os dados
    # preenchidos na pagina cadastrar.html
    ra_recebido = request.form['txtRA']
    nome_recebido = request.form['txtNome']
    idade_recebida = request.form['txtIdade']
    email_recebido = request.form['txtEmail']

    # a linha abaixo instancia um novo aluno
    novo_aluno = Aluno(ra_recebido, nome_recebido, 
                       idade_recebida, email_recebido)
    
    # a linha abaixo adiciona o novo aluno na lista
    lista_alunos_cadastrados.append(novo_aluno)
    return redirect('/lista')
    # a linha abaixo redireciona para a pagina lista.html


# a linha a baixo deve ser a ultima linha do projeto
app.run()

