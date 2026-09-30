from models.usuario import Usuario
from repository.usuario_repository import UsuarioRepository
from services.errors import ConflitoErro, ValidacaoErro


class UsuarioService:
    CAMPOS_OBRIGATORIOS = ("nome", "email", "senha", "tipo_usuario")

    @classmethod
    def _validar_dados(cls, dados):
        if not isinstance(dados, dict):
            raise ValidacaoErro("O corpo da requisição deve ser um objeto JSON")

        nomes = {
            "nome": "Nome",
            "email": "Email",
            "senha": "Senha",
            "tipo_usuario": "Tipo de usuário",
        }
        for campo in cls.CAMPOS_OBRIGATORIOS:
            if not isinstance(dados.get(campo), str) or not dados[campo].strip():
                raise ValidacaoErro(f"{nomes[campo]} é obrigatório")

        if "@" not in dados["email"]:
            raise ValidacaoErro("Email inválido")

    @classmethod
    def listar(cls):
        return UsuarioRepository.listar()

    @classmethod
    def buscar_por_id(cls, usuario_id):
        return UsuarioRepository.buscar_por_id(usuario_id)

    @classmethod
    def criar(cls, dados):
        cls._validar_dados(dados)
        email = dados["email"].strip().lower()
        if not UsuarioRepository.email_disponivel(email):
            raise ConflitoErro("Email já cadastrado")

        usuario = Usuario(
            nome=dados["nome"].strip(),
            email=email,
            senha=dados["senha"],
            tipo_usuario=dados["tipo_usuario"].strip(),
        )
        return UsuarioRepository.adicionar(usuario)

    @classmethod
    def atualizar(cls, usuario_id, dados):
        cls._validar_dados(dados)
        dados = dados.copy()
        dados["nome"] = dados["nome"].strip()
        dados["email"] = dados["email"].strip().lower()
        dados["tipo_usuario"] = dados["tipo_usuario"].strip()
        if not UsuarioRepository.email_disponivel(dados["email"], usuario_id):
            raise ConflitoErro("Email já cadastrado")
        return UsuarioRepository.atualizar(usuario_id, dados)

    @classmethod
    def remover(cls, usuario_id):
        return UsuarioRepository.remover(usuario_id)