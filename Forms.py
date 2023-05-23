from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class formLogin(FlaskForm):
    email   = StringField('email',validators=[DataRequired(),Email()])
    senha   = PasswordField('Senha', validators=[DataRequired(),Length(6)])
    submitLogin = SubmitField('Login')
    
    
class formNovoUsuario(FlaskForm):
    nome    = StringField('Nome', validators=[DataRequired()])
    enail   = StringField('Email', validators=[DataRequired(),Email()])
    celular = StringField('Celular', validators=[])
    cpf     = StringField('CPF', validatrs=[])
    senha   = PasswordField('Senha',validators=[DataRequired(),Length(6, 12)])
    senhaConfirmação = PasswordField('Confirmação de Senha', validators=[DataRequired(),EqualTo('senha')])
    submit  = SubmitField('Criar Conta')