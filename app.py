import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect, session
from forms import formLogin, formNovoUsuario
from hashlib import sha256

app = Flask(__name__)


app.config['SECRET_KEY'] = 'f03e83daa6c1bf312ffee9e3b8bc44743641579bad3aec5fd96d7d325485c184'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pw2010@@',
    database = 'ead_senac',
)


@app.route('/')
def index():
    title="Curso a EAD Senac"
    return render_template('index.html',title=title)


@app.route('/cursos')
def cursos():
    
    my_cursor = mydb.cursor()
    my_cursor.execute('select * from cursos')

    cursos = my_cursor.fetchall()


    return render_template('curso.html',cursos=cursos)


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/curso_a_distancia')
def ead():
    return render_template('sobreEAD.html')


@app.route('/login', methods=['get','post'])
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulário formulário de login'
    
    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()

    if form_login.validate_on_submit() and 'submitLogin' in request.form:
        
        cursor = mydb.cursor()

        email = form_login.email.data
        senha = form_login.senha.data
        hashSenha = sha256(senha.encode())

        comando = f'Select * from alunos where email = "{email}" '
        cursor.execute(comando)
        result = cursor.fetchall()

        if hashSenha.hexdigest() ==  result[0][5] :
            session['nome_usuario'] = result[0][1]
            flash(f'Login realizado com sucesso: {form_login.email.data}', 'alert-primary')
            return redirect(url_for('index'))
        else:
            flash(f'Usuario ou senha incorreta para: {form_login.email.data}', 'alert-danger')
            return redirect(url_for('login'))    
        


    if form_novo_usuario.validate_on_submit() and 'submitCadastro' in request.form:

        cursor = mydb.cursor()

        nome     = form_novo_usuario.nome.data
        telefone = form_novo_usuario.celular.data
        email    = form_novo_usuario.email.data
        cpf      = form_novo_usuario.cpf.data
        senha    = form_novo_usuario.senha.data
        hashSenha = sha256(senha.encode())
        
        query = f'INSERT INTO alunos (nome,email,celular,documento,senha) VALUES ("{nome}","{email}","{telefone}","{cpf}","{hashSenha.hexdigest()}")'
        print(query)
        cursor.execute(query)
        mydb.commit()

        flash(f'Cadastro realizado com sucesso: {form_novo_usuario.nome.data}' , 'alert-success')
        return redirect(url_for('index'))

    
    return render_template('loginObjeto.html',titulo=titulo,descricao=descricao,form_login=form_login,form_novo_usuario=form_novo_usuario)

@app.route('/logOut')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)