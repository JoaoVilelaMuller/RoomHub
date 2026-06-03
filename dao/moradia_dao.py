class MoradiaDAO:
    moradias = []

    @classmethod
    def listar(cls):
        return cls.moradias

    @classmethod
    def buscar_por_id(cls, id):
        for moradia in cls.moradias:
            if moradia.id == id:
                return moradia
        return None

    @classmethod
    def adicionar(cls, moradia):
        cls.moradias.append(moradia)

    @classmethod
    def remover(cls, id):
        moradia = cls.buscar_por_id(id)
        if moradia:
            cls.moradias.remove(moradia)
        return moradia