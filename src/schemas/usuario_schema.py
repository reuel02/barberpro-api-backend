from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.usuario import Usuario


class UsuarioSchema(SQLAlchemyAutoSchema):
    senha = fields.String(load_only=True, required=True)

    class Meta:
        model = Usuario
        load_instance = False
        dump_only = ("id", "empresa_id", "senha_hash", "role")
