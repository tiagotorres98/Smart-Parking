#from _typeshed import OpenBinaryMode, OpenBinaryModeReading
from flask import render_template #método para renderizar templates HTML
from flask import request
from app import app, db
from app.models.tables import Pessoa


@app.route("/")
def index():
    return "Hello mundo!"

@app.route("/register", methods=['POST', 'GET'])
def cadastrarUsuario(nome, dt_nascimento, sexo, cpf, rg):   
    nome = request.args.get('nome')
    dt_nascimento = request.args.get('dt_nascimento')
    sexo = request.args.get('sexo')
    cpf = request.args.get('cpf')
    rg = request.args.get('rg')

    person = Pessoa(nome, dt_nascimento, sexo, cpf, rg)
    
    db.session.add(person)
    db.session.commit()
    return "Pessoa criada com sucesso!"


a = """
@app.route('/aiai')
def teste():
    person = Pessoa('Marlon','1998/10/15','Masculino','123.456.789-0','123.456.789-X')

    db.session.add(person)
    db.session.commit()
    return "Pessoa criada com sucesso!"""

