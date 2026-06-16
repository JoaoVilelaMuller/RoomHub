class Avaliacao:
    def __init__(self, id, usuario_id, moradia_id, nota, comentario):
        self.id = id
        self.usuario_id = usuario_id
        self.moradia_id = moradia_id
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"Avaliacao(id={self.id}, nota={self.nota})"