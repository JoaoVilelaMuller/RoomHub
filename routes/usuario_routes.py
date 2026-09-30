from flask import Blueprint, jsonify, request

from services.errors import ConflitoErro, ValidacaoErro
from services.usuario_service import UsuarioService


usuario_bp = Blueprint("usuarios", __name__)


@usuario_bp.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(UsuarioService.listar())


@usuario_bp.route("/api/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario = UsuarioService.buscar_por_id(id)
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario)


@usuario_bp.route("/api/usuarios", methods=["POST"])
def criar_usuario():
    try:
        usuario = UsuarioService.criar(request.get_json())
    except ValidacaoErro as erro:
        return jsonify({"erro": str(erro)}), 400
    except ConflitoErro as erro:
        return jsonify({"erro": str(erro)}), 409
    return jsonify(usuario), 201


@usuario_bp.route("/api/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    usuario = UsuarioService.remover(id)
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario)


@usuario_bp.route("/api/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    try:
        usuario = UsuarioService.atualizar(id, request.get_json())
    except ValidacaoErro as erro:
        return jsonify({"erro": str(erro)}), 400
    except ConflitoErro as erro:
        return jsonify({"erro": str(erro)}), 409
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario)