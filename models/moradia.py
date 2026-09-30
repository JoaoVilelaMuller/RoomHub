from database import Base
from sqlalchemy import Column, Float, Integer, String, Text


class Moradia(Base):
    __tablename__ = "moradias"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text, nullable=False, default="")
    cidade = Column(String(100), nullable=False)
    universidade = Column(String(150), nullable=False)
    preco = Column(Float, nullable=False)

    def __init__(self, id=None, titulo=None, descricao="", cidade=None,
                 universidade=None, preco=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.cidade = cidade
        self.universidade = universidade
        self.preco = preco

    def __str__(self):
        return f"Moradia(id={self.id}, titulo={self.titulo})"

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "cidade": self.cidade,
            "universidade": self.universidade,
            "preco": self.preco
        }
