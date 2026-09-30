from dao.moradia_dao import MoradiaDAO


class MoradiaRepository:
    @classmethod
    def listar(cls):
        return [moradia.to_dict() for moradia in MoradiaDAO.listar()]

    @classmethod
    def buscar_por_id(cls, moradia_id):
        moradia = MoradiaDAO.buscar_por_id(moradia_id)
        return moradia.to_dict() if moradia else None

    @classmethod
    def adicionar(cls, moradia):
        return MoradiaDAO.adicionar(moradia).to_dict()

    @classmethod
    def atualizar(cls, moradia_id, dados):
        moradia = MoradiaDAO.atualizar(moradia_id, dados)
        return moradia.to_dict() if moradia else None

    @classmethod
    def remover(cls, moradia_id):
        moradia = MoradiaDAO.remover(moradia_id)
        return moradia.to_dict() if moradia else None