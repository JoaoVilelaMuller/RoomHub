class UsuarioDAO:
    usuarios = []

    @classmethod
    def listar(cls):
        return cls.usuarios

    @classmethod
    def buscar_por_id(cls, id):
        for usuario in cls.usuarios:
            if usuario.id == id:
                return usuario
        return None

    @classmethod
    def adicionar(cls, usuario):
        cls.usuarios.append(usuario)

    @classmethod
    def remover(cls, id):
        usuario = cls.buscar_por_id(id)
        if usuario:
            cls.usuarios.remove(usuario)
        return usuario