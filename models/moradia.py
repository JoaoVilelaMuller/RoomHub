class Moradia:
    def __init__(self, id, titulo, descricao, cidade, universidade, preco):

        if not titulo:
            raise ValueError("Título é obrigatório")

        if preco < 0:
            raise ValueError("Preço não pode ser negativo")

        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.cidade = cidade
        self.universidade = universidade
        self.preco = preco

    def __str__(self):
        return f"Moradia(id={self.id}, titulo={self.titulo})"

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "cidade": self.cidade,
            "universidade": self.universidade,
            "preco": self.preco
        }