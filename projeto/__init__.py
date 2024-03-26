from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# - Instânciar o inicio do app
app = Flask(__name__)
# - Inicializar o banco de dados
db = SQLAlchemy()
# - Instanciar a config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'
db.init_app(app)

from projeto import routes