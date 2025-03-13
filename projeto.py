from flask import Flask, render_template #importando biblioteca

# a linha a baixo cria a variavel de aplicação 
app = Flask(__name__)

# a linha a baixo cria uma rota

@app.route('/hello')
def ola ():
    return "<h2>Iniciando projeto com flask</h2>"

@app.route('/lista')
def lista_alunos():

    # a linha abaixo cria uma lista de alunos
    lista_alunos_cadastrados = ['Joaquim', 'Alisson', 
                                'Moisés', 'Manuela']

    return render_template("lista.html", titulo = "Unifecaf", alunos = lista_alunos_cadastrados) 


# a linha a baixo deve ser a ultima linha do projeto
app.run() 