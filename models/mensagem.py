class Mensagem:
    def __init__(self, id, remetente_id, destinatario_id, conteudo):
        self.id = id
        self.remetente_id = remetente_id
        self.destinatario_id = destinatario_id
        self.conteudo = conteudo

    def __str__(self):
        return f"Mensagem(id={self.id}, remetente={self.remetente_id})"