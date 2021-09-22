from os import set_inheritable
from app import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)
    fk_pessoa = db.Column(db.Integer, db.ForeignKey("pessoas.id_pessoa"))
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    pessoa = db.relationship("Pessoa", foreign_keys=fk_pessoa)

    def __init__(self, fk_pessoa, email, senha, tipo, status):
        self.fk_pessoa = fk_pessoa
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.status = status

    def __repr__(self):
        return "<Usuario %r>" % self.email


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(50), unique=True, nullable=False)
    rg = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, nome, dt_nascimento, sexo, cpf, rg):
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
    
    def __repr__(self):
        return "<Pessoa %r" % self.nome


class Telefone(db.Model):
    __tablename__ = "telefones"

    id_telefone = db.Column(db.Integer, primary_key=True)
    fk_pessoa = db.Column(db.Integer, db.ForeignKey("pessoas.id_pessoa"))
    tipo = db.Column(db.String(20), nullable=False)
    numero = db.Column(db.String(30), unique=True, nullable=False)
    descricao = db.Column(db.String(100), nullable=True)

    pessoa = db.relationship("Pessoa", foreign_keys=fk_pessoa)

    def __init__(self, fk_pessoa, tipo, numero, descricao):
        self.fk_pessoa = fk_pessoa(fk_pessoa)
        self.tipo = tipo
        self.numero = numero
        self.descricao = descricao
    
    def __repr__(self):
        return "<Telefone %r" % self.numero

class Endereco(db.Model):
    __tablename__ = "enderecos"

    id_endereco = db.Column(db.Integer, primary_key=True)
    fk_pessoa = db.Column(db.Integer, db.ForeignKey("pessoas.id_pessoa"))
    fk_cidade = db.Column(db.Integer, db.ForeignKey("cidades.id_cidade"))
    logradouro = db.Column(db.String(200), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(12), nullable=False)
    complemento = db.Column(db.String(200), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)

    pessoa = db.relationship("Pessoa", foreign_keys=fk_pessoa)
    cidade = db.relationship("Cidade", foreign_keys=fk_cidade)

    def __init__(self, fk_pessoa, fk_cidade, logradouro, bairro, numero, complemento, titulo):
        self.fk_pessoa = fk_pessoa
        self.fk_cidade = fk_cidade
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.titulo = titulo
    
    def __repr__(self):
        return "<Endereco %r" % self.logradouro

    
class Cidade(db.Model):
    __tablename__ = "cidades"

    id_cidade = db.Column(db.Integer, primary_key=True)
    fk_estado = db.Column(db.Integer, db.ForeignKey("estados.id_estado"))
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=True)

    estado = db.relationship("Estado", foreign_keys=fk_estado)

    def __init__(self, fk_estado, nome, descricao):
        self.fk_estado = fk_estado
        self.nome = nome
        self.descricao = descricao
    
    def __repr__(self):
        return "<Cidade %r" % self.nome


class Estado(db.Model):
    __tablename__ = "estados"

    id_estado = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, sigla, descricao):
        self.nome = nome
        self.sigla = sigla
        self.descricao = descricao

    def __repr__(self):
        return "<Estado %r" % self.nome

##/// finalização parte de usuário e pessoa


class Proprietario(db.Model):
    __tablename__ = "proprietarios"

    id_proprietario = db.Column(db.Integer, primary_key=True)
    fk_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id_usuario"))
    fk_estabelecimento = db.Column(db.Integer, db.ForeignKey("estabelecimentos.id_estabelecimento"))

    usuario = db.relationship("Usuario", foreign_keys=fk_usuario)
    estabelecimento = db.relationship("Estabelecimento", foreign_keys=fk_estabelecimento)

    def __init__(self, fk_usuario, fk_estabelecimento):
        self.fk_usuario = fk_usuario
        self.fk_estabelecimento = fk_estabelecimento

    def __repr__(self):
        return "<Estado %r" % self.id_proprietario

class Estabelecimento(db.Model):
    __tablename__ = "estabelecimentos"

    id_estabelecimento = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(200), nullable=False)
    nome = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, razao_social, nome, cnpj):
        self.razao_social = razao_social
        self.nome = nome
        self.cnpj = cnpj

    def __repr__(self):
        return "<Estabelecimento %r" % self.razao_social

class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id_veiculo = db.Column(db.Integer, primary_key=True)
    fk_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id_usuario")) 
    fk_modelo = db.Column(db.Integer, db.ForeignKey("modelos_veiculos.id_modelo_veiculo")) 
    placa = db.Column(db.String(40), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    renavam = db.Column(db.String(60), unique=True, nullable=False)
    chassi = db.Column(db.String(60), unique=True, nullable=False)

    usuario = db.relationship("Usuario", foreign_keys=fk_usuario)
    modelo = db.relationship("Modelo_Veiculo", foreign_keys=fk_modelo)

    def __init__(self,fk_usuario, fk_modelo, placa, cor, renavam, chassi):
        self.fk_usuario = fk_usuario
        self.fk_modelo = fk_modelo
        self.placa = placa
        self.cor = cor
        self.renavam = renavam
        self.chassi = chassi

    def __repr__(self):
        return "<Veiculo %r" % self.placa

class Modelo_Veiculo(db.Model):
    __tablename__ = "modelos_veiculos"

    id_modelo_veiculo = db.Column(db.Integer, primary_key=True)
    fk_marca_veiculo = db.Column(db.Integer, db.ForeignKey("marcas_veiculos.id_marca_veiculo")) 
    fk_categoria_veiculo = db.Column(db.Integer, db.ForeignKey("categorias_veiculos.id_categoria_veiculo")) 
    nome = db.Column(db.String(40), nullable=True)
    descricao = db.Column(db.String(100), nullable=True)

    marca_veiculo = db.relationship("Marca_Veiculo", foreign_keys=fk_marca_veiculo)
    categoria_veiculo = db.relationship("Categoria_Veiculo", foreign_keys=fk_categoria_veiculo)

    def __init__(self, fk_marca_veiculo, fk_categoria_veiculo, nome, descricao):
        self.fk_marca_veiculo = fk_marca_veiculo
        self.fk_categoria_veiculo = fk_categoria_veiculo
        self.nome = nome
        self.descricao = descricao


    def __repr__(self):
        return "<Modelo_Veiculo %r" % self.nome  


class Categoria_Veiculo(db.Model):
    __tablename__ = "categorias_veiculos"

    id_categoria_veiculo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=False)
    descricao = db.Column(db.String(40), nullable=False)

    def __init__(self, id_categoria_veiculo, nome, descricao):
        self.id_categoria_veiculo = id_categoria_veiculo
        self.nome = nome
        self.descricao = descricao
    
    def __repr__(self):
        return "<Categoria_Veiculo %r" % self.nome

class Marca_Veiculo(db.Model):
    __tablename__ = "marcas_veiculos"

    id_marca_veiculo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=False)
    descricao = db.Column(db.String(40), nullable=False)

    def __init__(self, id_marca_veiculo, nome, descricao):
        self.id_marca_veiculo = id_marca_veiculo
        self.nome = nome
        self.descricao = descricao
    
    def __repr__(self):
        return "<Marca_Veiculo %r" % self.nome    

####  Tabelas específicas de locação

class Locacao(db.Model):
    __tablename__ = "locacoes"

    id_locacao = db.Column(db.Integer, primary_key=True)
    fk_forma_pagamento = db.Column(db.Integer, db.ForeignKey("formas_pagamento.id_forma_pagamento")) 
    fk_veiculo = db.Column(db.Integer, db.ForeignKey("veiculos.id_veiculo")) 
    fk_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id_usuario")) 
    fk_vaga = db.Column(db.Integer, db.ForeignKey("vagas.id_vaga")) 
    hora_entrada = db.Column(db.DateTime, nullable=False)
    hora_saida = db.Column(db.DateTime, nullable=False)
    valor_hora = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(400), nullable=False)

    forma_pagamento = db.relationship("Forma_Pagamento", foreign_keys=fk_forma_pagamento)
    veiculo = db.relationship("Veiculo", foreign_keys=fk_veiculo)
    usuario = db.relationship("Usuario", foreign_keys=fk_usuario)
    vaga = db.relationship("Vaga", foreign_keys=fk_vaga)
    
    def __init__(self, fk_forma_pagamento, fk_veiculo, fk_usuario, fk_vaga, hora_entrada, hora_saida, valor_hora, descricao):
        self.fk_forma_pagamento = fk_forma_pagamento
        self.fk_veiculo = fk_veiculo
        self.fk_usuario = fk_usuario
        self.fk_vaga = fk_vaga
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.valor_hora = valor_hora
        self.descricao = descricao

    def __repr__(self):
        return "<Locacao %r" % self.id_locacao            

class Servico_Locacao(db.Model):
    __tablename__ = "servicos_locacao"

    id_servico_locacao = db.Column(db.Integer, primary_key=True)
    fk_locacao = db.Column(db.Integer, db.ForeignKey("locacoes.id_locacao")) 
    fk_servico = db.Column(db.Integer, db.ForeignKey("servicos.id_servico")) 
    status = db.Column(db.Boolean, nullable=False)
    descricao = db.Column(db.String(500), nullable=False)

    locacao = db.relationship("Locacao", foreign_keys=fk_locacao)
    servico = db.relationship("Servico", foreign_keys=fk_servico)

    def __init__(self, fk_locacao, fk_servico, status, descricao):
        self.fk_locacao = fk_locacao
        self.fk_servico = fk_servico
        self.status = status
        self.descricao = descricao

    def __repr__(self):
        return "<Servico_Locacao %r" % self.id_servico_locacao
 
class Servico(db.Model):
    __tablename__ = "servicos"

    id_servico = db.Column(db.Integer, primary_key=True)
    fk_categoria_servico = db.Column(db.Integer, db.ForeignKey("categorias_servicos.id_categoria_servico")) 
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    categoria_servico = db.relationship("Categoria_Servico", foreign_keys=fk_categoria_servico)

    def __init__(self, fk_categoria_servico, nome, descricao, valor):
        self.fk_categoria_servico = fk_categoria_servico
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def __repr__(self):
        return "<Servico %r" % self.nome

class Categoria_Servico(db.Model):
    __tablename__ = "categorias_servicos"

    id_categoria_servico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "<Categoria_Servico %r" % self.nome


class Forma_Pagamento(db.Model):
    __tablename__ = "formas_pagamento"

    id_forma_pagamento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "<Forma_Pagamento %r" % self.nome

class Vaga(db.Model):
    __tablename__ = "vagas"

    id_vaga = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    andar = db.Column(db.String(10), nullable=False)
    localizacao = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    descricao = db.Column(db.String(500), nullable=True)

    def __init__(self, nome, andar, localizacao, status, descricao):
        self.nome = nome
        self.andar = andar
        self.localizacao = localizacao
        self.status = status
        self.descricao = descricao

    def __repr__(self):
        return "<Vaga %r" % self.nome

class Sensor(db.Model):
    __tablename__ = "sensores"

    id_sensor = db.Column(db.Integer, primary_key=True)
    fk_tipo_sensor = db.Column(db.Integer, db.ForeignKey("tipos_sensores.id_tipo_sensor")) 
    fk_vaga = db.Column(db.Integer, db.ForeignKey("vagas.id_vaga")) 
    nome = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    modelo = db.Column(db.String(200), nullable=False)
    observacoes = db.Column(db.String(500), nullable=False)

    tipo_sensor = db.relationship("Tipo_Sensor", foreign_keys=fk_tipo_sensor)
    vaga = db.relationship("Vaga", foreign_keys=fk_vaga)

    def __init__(self, fk_tipo_sensor, fk_vaga, nome, status, modelo, observacoes):
        self.fk_tipo_sensor = fk_tipo_sensor
        self.fk_vaga = fk_vaga
        self.nome = nome
        self.status = status
        self.modelo = modelo
        self.observacoes = observacoes

    def __repr__(self):
        return "<Vaga %r" % self.nome

class Tipo_Sensor(db.Model):
    __tablename__ = "tipos_sensores"
    
    id_tipo_sensor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __init__(self, id_tipo_sensor, nome, descricao):
        self.id_tipo_sensor = id_tipo_sensor
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "<Tipo_Sensor %r" % self.nome
