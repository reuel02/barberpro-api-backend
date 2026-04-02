from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.agendamento import Agendamento

class AgendamentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Agendamento 
        load_instance = True 
