from database import Base
from sqlalchemy import Column, Integer, String


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    tipo_usuario = Column(String(50), nullable=False)

    def __init__(self, id=None, nome=None, email=None, senha=None, tipo_usuario=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        return f"Usuario(id={self.id}, nome={self.nome})"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo_usuario": self.tipo_usuario
        }
