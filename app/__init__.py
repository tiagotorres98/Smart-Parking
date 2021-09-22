from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from urllib.parse import quote_plus
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')

import pandas as pd 

db = SQLAlchemy(app)
migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default
