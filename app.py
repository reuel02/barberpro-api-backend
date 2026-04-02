from flask import Flask
from db import db
from flask_migrate import Migrate
from src.routes.agendamentos_routes import agendamentos_bp
import src.models

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:8081/barbearia_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conecta o banco de dados à aplicação
db.init_app(app)

# Instancia e conecta o alembic
migrate = Migrate(app, db)

# Registra o Blueprint das rotas, atribuindo um prefixo
app.register_blueprint(agendamentos_bp, url_prefix='/api/agendamentos')

if __name__ == '__main__':

    app.run(debug=True)
