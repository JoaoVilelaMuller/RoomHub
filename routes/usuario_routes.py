from flask import Blueprint, jsonify, request
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario



usuario_bp = Blueprint("usuarios", __name__)



@usuario_bp.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify([u.__dict__ for u in UsuarioDAO.listar()])



@usuario_bp.route("/api/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario = UsuarioDAO.buscar_por_id(id)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify(usuario.__dict__)



@usuario_bp.route("/api/usuarios", methods=["POST"])
def criar_usuario():

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    if not dados.get("nome"):
        return jsonify({"erro": "Nome é obrigatório"}), 400

    if not dados.get("email"):
        return jsonify({"erro": "Email é obrigatório"}), 400

    if not dados.get("senha"):
        return jsonify({"erro": "Senha é obrigatória"}), 400

    if not dados.get("tipo_usuario"):
        return jsonify({"erro": "Tipo de usuário é obrigatório"}), 400

    usuario = Usuario(
        dados["id"],
        dados["nome"],
        dados["email"],
        dados["senha"],
        dados["tipo_usuario"]
    )

    UsuarioDAO.adicionar(usuario)

    return jsonify(usuario.__dict__), 201



@usuario_bp.route("/api/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    usuario = UsuarioDAO.remover(id)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify(usuario.__dict__)



@usuario_bp.route("/api/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    if not dados.get("nome"):
        return jsonify({"erro": "Nome é obrigatório"}), 400

    if not dados.get("email"):
        return jsonify({"erro": "Email é obrigatório"}), 400

    usuario = UsuarioDAO.atualizar(id, dados)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify(usuario.__dict__)