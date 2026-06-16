class Anuncio:
    def __init__(self, id, usuario_id, moradia_id, data_publicacao):
        self.id = id
        self.usuario_id = usuario_id
        self.moradia_id = moradia_id
        self.data_publicacao = data_publicacao

    def __str__(self):
        return f"Anuncio(id={self.id}, moradia_id={self.moradia_id})"