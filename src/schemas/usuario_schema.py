from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.usuario import Usuario

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario 
        load_instance = True 