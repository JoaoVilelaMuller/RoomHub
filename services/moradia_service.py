import math

from models.moradia import Moradia
from repository.moradia_repository import MoradiaRepository
from services.errors import ValidacaoErro


class MoradiaService:
    CAMPOS_OBRIGATORIOS = ("titulo", "cidade", "universidade", "preco")

    @classmethod
    def _validar_dados(cls, dados):
        if not isinstance(dados, dict):
            raise ValidacaoErro("O corpo da requisição deve ser um objeto JSON")

        nomes = {
            "titulo": "Título",
            "cidade": "Cidade",
            "universidade": "Universidade",
            "preco": "Preço",
        }
        for campo in cls.CAMPOS_OBRIGATORIOS:
            if campo not in dados or dados[campo] is None:
                raise ValidacaoErro(f"{nomes[campo]} é obrigatório")
            if campo != "preco" and (
                not isinstance(dados[campo], str) or not dados[campo].strip()
            ):
                raise ValidacaoErro(f"{nomes[campo]} é obrigatório")

        preco = dados["preco"]
        if isinstance(preco, bool) or not isinstance(preco, (int, float)):
            raise ValidacaoErro("Preço inválido")
        if not math.isfinite(preco) or preco < 0:
            raise ValidacaoErro("Preço inválido")
        if not isinstance(dados.get("descricao", ""), str):
            raise ValidacaoErro("Descrição inválida")

    @classmethod
    def listar(cls):
        return MoradiaRepository.listar()

    @classmethod
    def buscar_por_id(cls, moradia_id):
        return MoradiaRepository.buscar_por_id(moradia_id)

    @classmethod
    def criar(cls, dados):
        cls._validar_dados(dados)
        moradia = Moradia(
            titulo=dados["titulo"].strip(),
            descricao=dados.get("descricao", ""),
            cidade=dados["cidade"].strip(),
            universidade=dados["universidade"].strip(),
            preco=dados["preco"],
        )
        return MoradiaRepository.adicionar(moradia)

    @classmethod
    def atualizar(cls, moradia_id, dados):
        cls._validar_dados(dados)
        dados = dados.copy()
        for campo in ("titulo", "cidade", "universidade"):
            dados[campo] = dados[campo].strip()
        dados.setdefault("descricao", "")
        return MoradiaRepository.atualizar(moradia_id, dados)

    @classmethod
    def remover(cls, moradia_id):
        return MoradiaRepository.remover(moradia_id)