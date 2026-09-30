import database
from models.usuario import Usuario


class UsuarioDAO:
    @classmethod
    def listar(cls):
        session = database.SessionLocal()
        try:
            return session.query(Usuario).order_by(Usuario.id).all()
        finally:
            session.close()

    @classmethod
    def buscar_por_id(cls, id):
        session = database.SessionLocal()
        try:
            return session.get(Usuario, id)
        finally:
            session.close()

    @classmethod
    def buscar_por_email(cls, email):
        session = database.SessionLocal()
        try:
            return session.query(Usuario).filter_by(email=email).first()
        finally:
            session.close()

    @classmethod
    def adicionar(cls, usuario):
        session = database.SessionLocal()
        try:
            session.add(usuario)
            session.commit()
            return usuario
        finally:
            session.close()

    @classmethod
    def atualizar(cls, id, dados):
        session = database.SessionLocal()
        try:
            usuario = session.get(Usuario, id)
            if usuario:
                usuario.nome = dados["nome"]
                usuario.email = dados["email"]
                usuario.senha = dados["senha"]
                usuario.tipo_usuario = dados["tipo_usuario"]
                session.commit()
            return usuario
        finally:
            session.close()

    @classmethod
    def remover(cls, id):
        session = database.SessionLocal()
        try:
            usuario = session.get(Usuario, id)
            if usuario:
                session.delete(usuario)
                session.commit()
            return usuario
        finally:
            session.close()

    @classmethod
