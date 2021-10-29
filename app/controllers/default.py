#from _typeshed import OpenBinaryMode, OpenBinaryModeReading
from flask import render_template #método para renderizar templates HTML
from flask import request
from app import app, db
from app.models.tables import *
import datetime as dt

@app.route("/")
def index():
    return "Hello mundo!"

#Início das rotas

@app.route("/register", methods=['POST', 'GET'])
def cadastrarUsuario(nome, dt_nascimento, sexo, cpf, rg):   
    nome = request.args.get('nome')
    email = request.args.get('email')
    endereco = request.args.get('endereco')
    sexo = request.args.get('sexo')
    CPF = request.args.get('cpf')
    rg = request.args.get('rg')
    dt_nascimento = request.args.get('dt_nascimento')

    senha = request.args.get('senha')
    tipo = request.args.get('tipo')
    status = request.args.get('status')
    
    person = Person(nome, dt_nascimento, sexo, cpf, rg)

    db.session.add(person)
    db.session.commit()

    usuario = User(person.id_pessoa, email, senha, tipo, status)

    db.session.add(usuario)
    db.session.commit()

    return "Cadastro criado com sucesso!"


@app.route("/estacionamentos", methods=['GET'])
def estacionamentos():
    return db.Estabelecimento.list()


@app.route("/estacionamento", methods=['POST', 'GET'])
def estacionamento():
    id_estabelecimento = request.args.get('id_estabelecimento')
    return db.Estabelecimento.filter(by='id_estabelecimento')


@app.route("/confirmar-aluguel", methods=['POST', 'GET'])
def confirmar_aluguel():
    id_estabelecimento = request.args.get('id_estabelecimento')
    fk_veiculo = request.args.get('fk_veiculo')
    fk_vaga = request.args.get('fk_vaga')
    fk_usuario = request.args.get('fk_usuario')
    fk_forma_pagamento = request.args.get('id_forma_pagamento')
    hora_entrada = request.args.get('hora_entrada')
    hora_saida = request.args.get('hora_saida')
    valor_hora = request.args.get('valor_hora')
    desc = request.args.get('desc')


    locacao = Rent(fk_forma_pagamento, fk_veiculo, fk_usuario, fk_vaga, hora_entrada, hora_saida, valor_hora, descricao)

    db.session.add(locacao)
    db.session.commit()

    return db.Estabelecimento.filter(by='id_estabelecimento')


@app.route("/vagas", methods=['POST'])
def vagas():
    id_estabelecimento = request.args.get('id_estabelecimento')
    return db.Vagas.filter(by=id_estabelecimento)




@app.route("/avaliacao", methods=['POST', 'GET'])
def avaliacao():
    id_estabelecimento = request.args.get('id_estabelecimento')
    nota = request.args.get('nota')
    avaliacao = request.args.get('avaliacao')

    return db.Estabelecimento.filter(by='id_estabelecimento')



class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "flasksqlalchemy-tutorial-users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    bio = db.Column(db.Text, index=False, unique=False, nullable=True)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)



@app.route("/", methods=["GET"])
def user_records():
    """Create a user via query string parameters."""
    username = request.args.get("user")
    email = request.args.get("email")
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return "already created!"
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
            on the playground is where I spent most of my days",
            admin=False,
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return render_template("users.jinja2", users=User.query.all(), title="Show Users")


