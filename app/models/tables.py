from os import set_inheritable
from app import db

class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True)
    fk_person = db.Column(db.Integer, db.ForeignKey("person.id_person"))
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    person = db.relationship("Person", foreign_keys=fk_person)

    def __init__(self, fk_person, email, password, type, status):
        self.fk_person = fk_person
        self.email = email
        self.password = password
        self.type = type
        self.status = status

    def __repr__(self):
        return "<User %r>" % self.email

class Person(db.Model):
    __tablename__ = "person"
    
    id_person = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(50), unique=True, nullable=False)
    rg = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name, birth_date, sexo, cpf, rg):
        self.name = name
        self.birth_date = birth_date
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
    
    def __repr__(self):
        return "<Person %r" % self.name

class Telephone(db.Model):
    __tablename__ = "telephones"

    id_telephone = db.Column(db.Integer, primary_key=True)
    fk_person = db.Column(db.Integer, db.ForeignKey("person.id_person"))
    type = db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String(100), nullable=True)

    person = db.relationship("Person", foreign_keys=fk_person)

    def __init__(self, fk_person, type, number, desc):
        self.fk_person = fk_person
        self.type = type
        self.number = number
        self.desc = desc

    def __repr__(self):
        return "<Telephone %r" % self.number

class Address(db.Model):
    __tablename__ = "addresses"

    id_address = db.Column(db.Integer, primary_key=True)
    fk_person = db.Column(db.Integer, db.ForeignKey("person.id_person"))
    fk_city = db.Column(db.Integer, db.ForeignKey("cities.id_city"))
    public_place = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(12), nullable=False)
    complement = db.Column(db.String(200), nullable=False)

    person = db.relationship("Person", foreign_keys=fk_person)
    city = db.relationship("City", foreign_keys=fk_city)

    def __init__(self, fk_person, fk_city, public_place, district, number, complement, titulo):
        self.fk_person = fk_person
        self.fk_city = fk_city
        self.public_place = public_place
        self.district = district
        self.number = number
        self.complement = complement
        self.titulo = titulo
    
    def __repr__(self):
        return "<Endereco %r" % self.public_place

class City(db.Model):
    __tablename__ = "cities"

    id_city = db.Column(db.Integer, primary_key=True)
    fk_state = db.Column(db.Integer, db.ForeignKey("states.id_state"))
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=True)

    state = db.relationship("State", foreign_keys=fk_state)

    def __init__(self, fk_state, name, desc):
        self.fk_state = fk_state
        self.name = name
        self.desc = desc
    
    def __repr__(self):
        return "<City %r" % self.name

class State(db.Model):
    __tablename__ = "states"

    id_state = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    initials = db.Column(db.String(10), nullable=False)  #sigla
    desc = db.Column(db.String(100), nullable=False)  #descrição

    def __init__(self, name, initials, desc):
        self.name = name
        self.initials = initials
        self.desc = desc

    def __repr__(self):
        return "<State %r" % self.name

##/// finalização parte de usuário e person


class Owner(db.Model):
    __tablename__ = "owners"

    id_owner = db.Column(db.Integer, primary_key=True)
    fk_user = db.Column(db.Integer, db.ForeignKey("users.id_user"))
    fk_establishment = db.Column(db.Integer, db.ForeignKey("establishments.id_establishment"))

    user = db.relationship("User", foreign_keys=fk_user)
    establishment = db.relationship("Establishment", foreign_keys=fk_establishment)

    def __init__(self, fk_user, fk_establishment):
        self.fk_user = fk_user
        self.fk_establishment = fk_establishment

    def __repr__(self):
        return "<State %r" % self.id_owner

class Establishment(db.Model):
    __tablename__ = "establishments"

    id_establishment = db.Column(db.Integer, primary_key=True)
    social_reason = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, social_reason, name, cnpj):
        self.social_reason = social_reason
        self.name = name
        self.cnpj = cnpj

    def __repr__(self):
        return "<Establishment %r" % self.social_reason

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id_vehicle = db.Column(db.Integer, primary_key=True)
    fk_user = db.Column(db.Integer, db.ForeignKey("users.id_user")) 
    fk_model = db.Column(db.Integer, db.ForeignKey("vehicle_models.id_modelo_vehicle")) 
    plate = db.Column(db.String(40), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    renavam = db.Column(db.String(60), unique=True, nullable=False)
    chassi = db.Column(db.String(60), unique=True, nullable=False)

    user = db.relationship("User", foreign_keys=fk_user)
    modelo = db.relationship("Vehicle_model", foreign_keys=fk_model)

    def __init__(self,fk_user, fk_model, plate, color, renavam, chassi):
        self.fk_user = fk_user
        self.fk_model = fk_model
        self.plate = plate
        self.color = color
        self.renavam = renavam
        self.chassi = chassi

    def __repr__(self):
        return "<Vehicle %r" % self.plate

class Vehicle_Model(db.Model):
    __tablename__ = "vehicle_models"

    id_modelo_vehicle = db.Column(db.Integer, primary_key=True)
    fk_vehicle_brand = db.Column(db.Integer, db.ForeignKey("vehicles_brands.id_vehicle_brand")) 
    fk_vehicle_category = db.Column(db.Integer, db.ForeignKey("vehicle_category.id_vehicle_category")) 
    name = db.Column(db.String(40), nullable=True)
    desc = db.Column(db.String(100), nullable=True)

    vehicle_brand = db.relationship("Vehicle_Brand", foreign_keys=fk_vehicle_brand)
    vehicle_category = db.relationship("Vehicle_Category", foreign_keys=fk_vehicle_category)

    def __init__(self, fk_vehicle_brand, fk_vehicle_category, name, desc):
        self.fk_vehicle_brand = fk_vehicle_brand
        self.fk_vehicle_category = fk_vehicle_category
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Vehicle_model %r" % self.name  

class Vehicle_Category(db.Model):
    __tablename__ = "vehicle_category"

    id_vehicle_category = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    desc = db.Column(db.String(40), nullable=False)

    def __init__(self, id_vehicle_category, name, desc):
        self.id_vehicle_category = id_vehicle_category
        self.name = name
        self.desc = desc
    
    def __repr__(self):
        return "<Vehicle_Category %r" % self.name

class Vehicle_Brand(db.Model):
    __tablename__ = "vehicles_brands"

    id_vehicle_brand = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    desc = db.Column(db.String(40), nullable=False)

    def __init__(self, id_vehicle_brand, name, desc):
        self.id_vehicle_brand = id_vehicle_brand
        self.name = name
        self.desc = desc
    
    def __repr__(self):
        return "<Vehicle_Brand %r" % self.name    

####  Tabelas específicas de locação

class Rent(db.Model):
    __tablename__ = "rents"

    id_rent = db.Column(db.Integer, primary_key=True)
    fk_payment_method = db.Column(db.Integer, db.ForeignKey("payment_method.id_payment_method")) 
    fk_vehicle = db.Column(db.Integer, db.ForeignKey("vehicles.id_vehicle")) 
    fk_user = db.Column(db.Integer, db.ForeignKey("users.id_user")) 
    fk_parking_space = db.Column(db.Integer, db.ForeignKey("parking_spaces.id_parking_space")) 
    entry_time = db.Column(db.DateTime, nullable=False)
    exit_time = db.Column(db.DateTime, nullable=False)
    hourly_value = db.Column(db.Float, nullable=False)
    desc = db.Column(db.String(400), nullable=False)

    payment_method = db.relationship("Payment_Method", foreign_keys=fk_payment_method)
    vehicle = db.relationship("Vehicle", foreign_keys=fk_vehicle)
    user = db.relationship("User", foreign_keys=fk_user)
    parking_space = db.relationship("Parking_Space", foreign_keys=fk_parking_space)
    
    def __init__(self, fk_payment_method, fk_vehicle, fk_user, fk_parking_space, entry_time, exit_time, hourly_value, desc):
        self.fk_payment_method = fk_payment_method
        self.fk_vehicle = fk_vehicle
        self.fk_user = fk_user
        self.fk_parking_space = fk_parking_space
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.hourly_value = hourly_value
        self.desc = desc

    def __repr__(self):
        return "<Rent %r" % self.id_rent        

class Rent_Service(db.Model):
    __tablename__ = "services_rental"

    id_service_rent = db.Column(db.Integer, primary_key=True)
    fk_rent = db.Column(db.Integer, db.ForeignKey("rents.id_rent")) 
    fk_service = db.Column(db.Integer, db.ForeignKey("services.id_service")) 
    status = db.Column(db.Boolean, nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    rental = db.relationship("Leases", foreign_keys=fk_rent)
    service = db.relationship("Service", foreign_keys=fk_service)

    def __init__(self, fk_rent, fk_service, status, desc):
        self.fk_rent = fk_rent
        self.fk_service = fk_service
        self.status = status
        self.desc = desc

    def __repr__(self):
        return "<Rent_Service %r" % self.id_service_rent
 
class Service(db.Model):
    __tablename__ = "services"

    id_service = db.Column(db.Integer, primary_key=True)
    fk_service_category = db.Column(db.Integer, db.ForeignKey("service_category.id_service_category")) 
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    service_category = db.relationship("Service_Category", foreign_keys=fk_service_category)

    def __init__(self, fk_service_category, name, desc, valor):
        self.fk_service_category = fk_service_category
        self.name = name
        self.desc = desc
        self.valor = valor

    def __repr__(self):
        return "<Service %r" % self.name

class Service_Category(db.Model):
    __tablename__ = "service_category"

    id_service_category = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Service_Category %r" % self.name


class Payment_Method(db.Model):
    __tablename__ = "payment_method"

    id_payment_method = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(500), nullable=True)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Payment_Method %r" % self.name

class Parking_Space(db.Model):
    __tablename__ = "parking_spaces"

    id_parking_space = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    floor = db.Column(db.String(10), nullable=False)
    localization = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    desc = db.Column(db.String(500), nullable=True)

    def __init__(self, name, floor, localization, status, desc):
        self.name = name
        self.floor = floor
        self.localization = localization
        self.status = status
        self.desc = desc

    def __repr__(self):
        return "<Parking_Space %r" % self.name

class Sensor(db.Model):
    __tablename__ = "sensors"

    id_sensor = db.Column(db.Integer, primary_key=True)
    fk_sensor_type = db.Column(db.Integer, db.ForeignKey("sensors_types.id_sensor_type")) 
    fk_parking_space = db.Column(db.Integer, db.ForeignKey("parking_spaces.id_parking_space")) 
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    modelo = db.Column(db.String(200), nullable=False)
    observacoes = db.Column(db.String(500), nullable=False)

    sensor_type = db.relationship("Sensor_Type", foreign_keys=fk_sensor_type)
    parking_space = db.relationship("Parking_Space", foreign_keys=fk_parking_space)

    def __init__(self, fk_sensor_type, fk_parking_space, name, status, modelo, observacoes):
        self.fk_sensor_type = fk_sensor_type
        self.fk_parking_space = fk_parking_space
        self.name = name
        self.status = status
        self.modelo = modelo
        self.observacoes = observacoes

    def __repr__(self):
        return "<Sensor %r" % self.name

class Sensor_Type(db.Model):
    __tablename__ = "sensors_types"
    
    id_sensor_type = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    def __init__(self, id_sensor_type, name, desc):
        self.id_sensor_type = id_sensor_type
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Sensor_Type %r" % self.name