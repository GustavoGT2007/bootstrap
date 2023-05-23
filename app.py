from flask import Flask, render_template, request
from Forms import formLogin, formNovoUsuario

app = Flask(__name__)

app.config['SECRET_KEY'] = '75f50e1c633458f6ef35fdf85df89098'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/ead')
def ead():
    return render_template('ead.html')


@app.route('/login', methods=['get','post'])
def login():
    titulo = 'Login formulario de login'
    descricao = 'Formulario formulario de login'
    
    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()
    
    return render_template('loginObjeto.html',titulo=titulo,descricao=descricao,foem_login=form_login,form_novo_usuario=form_novo_usuario)

if __name__ == '__main__':
    app.run(debug=True)