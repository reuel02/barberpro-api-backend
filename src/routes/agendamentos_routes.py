from src.controllers.agendamentos.listar_agendamentos import listar_agendamentos
from flask import Blueprint

# Criacao da instancia do Blueprint de agendamentos
agendamentos_bp = Blueprint('agendamentos', __name__)

# Rota de listagem de agendamentos
agendamentos_bp.route('/', methods=['GET'])(listar_agendamentos)