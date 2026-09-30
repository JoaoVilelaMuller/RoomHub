from dao.usuario_dao import UsuarioDAO


class UsuarioRepository:
    @classmethod
    def listar(cls):
        return [usuario.to_dict() for usuario in UsuarioDAO.listar()]

    @classmethod
    def buscar_por_id(cls, usuario_id):
        usuario = UsuarioDAO.buscar_por_id(usuario_id)
        return usuario.to_dict() if usuario else None

    @classmethod
    def email_disponivel(cls, email, usuario_id=None):
        usuario = UsuarioDAO.buscar_por_email(email)
        return usuario is None or usuario.id == usuario_id

    @classmethod
    def adicionar(cls, usuario):
        return UsuarioDAO.adicionar(usuario).to_dict()

    @classmethod
    def atualizar(cls, usuario_id, dados):
        usuario = UsuarioDAO.atualizar(usuario_id, dados)
        return usuario.to_dict() if usuario else None

    @classmethod
    def remover(cls, usuario_id):
        usuario = UsuarioDAO.remover(usuario_id)
        return usuario.to_dict() if usuario else None