import database
from models.moradia import Moradia


class MoradiaDAO:
    @classmethod
    def listar(cls):
        session = database.SessionLocal()
        try:
            return session.query(Moradia).order_by(Moradia.id).all()
        finally:
            session.close()

    @classmethod
    def buscar_por_id(cls, id):
        session = database.SessionLocal()
        try:
            return session.get(Moradia, id)
        finally:
            session.close()

    @classmethod
    def adicionar(cls, moradia):
        session = database.SessionLocal()
        try:
            session.add(moradia)
            session.commit()
            return moradia
        finally:
            session.close()

    @classmethod
    def atualizar(cls, id, dados):
        session = database.SessionLocal()
        try:
            moradia = session.get(Moradia, id)
            if moradia:
                moradia.titulo = dados["titulo"]
                moradia.descricao = dados["descricao"]
                moradia.cidade = dados["cidade"]
                moradia.universidade = dados["universidade"]
                moradia.preco = dados["preco"]
                session.commit()
            return moradia
        finally:
            session.close()

    @classmethod
    def remover(cls, id):
        session = database.SessionLocal()
        try:
            moradia = session.get(Moradia, id)
            if moradia:
                session.delete(moradia)
                session.commit()
            return moradia
        finally:
            session.close()
