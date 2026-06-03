class Moradia:
    def __init__(self, id, titulo, descricao, cidade, universidade, preco):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.cidade = cidade
        self.universidade = universidade
        self.preco = preco

    def __str__(self):
        return f"Moradia(id={self.id}, titulo={self.titulo})"