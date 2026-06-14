class Usuario:
    def __init__(self, id, nome, email, senha, tipo_usuario):

        if not nome:
            raise ValueError("Nome é obrigatório")

        if not email:
            raise ValueError("Email é obrigatório")

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