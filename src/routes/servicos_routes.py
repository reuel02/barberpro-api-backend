from src.controllers.servicos.cadastrar_servico import cadastrar_servico
from flask import Blueprint

# Criacao da instancia do Blueprint de servicos
servicos_bp = Blueprint('servicos', __name__)

# Rota de cadastro de servicos
servicos_bp.route('/cadastrar', methods=['POST'])(cadastrar_servico)