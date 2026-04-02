from flask import jsonify

# Controlador de listar agendamentos
def listar_agendamentos():
    dados = [
        {"id": 1, "cliente": "João", "servico": "Corte de cabelo"},
        {"id": 2, "cliente": "Maria", "servico": "Sobrancelha"}
    ]

    return jsonify({
        "sucesso": True,
        "dados": dados
    }), 200