from flask import Blueprint, jsonify, request

from services.errors import ValidacaoErro
from services.moradia_service import MoradiaService


moradia_bp = Blueprint("moradias", __name__)


@moradia_bp.route("/api/moradias", methods=["GET"])
def listar_moradias():
    return jsonify(MoradiaService.listar())


@moradia_bp.route("/api/moradias/<int:id>", methods=["GET"])
def buscar_moradia(id):
    moradia = MoradiaService.buscar_por_id(id)
    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404
    return jsonify(moradia)


@moradia_bp.route("/api/moradias", methods=["POST"])
def criar_moradia():
    try:
        moradia = MoradiaService.criar(request.get_json())
    except ValidacaoErro as erro:
        return jsonify({"erro": str(erro)}), 400
    return jsonify(moradia), 201


@moradia_bp.route("/api/moradias/<int:id>", methods=["DELETE"])
def excluir_moradia(id):
    moradia = MoradiaService.remover(id)
    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404
    return jsonify(moradia)


@moradia_bp.route("/api/moradias/<int:id>", methods=["PUT"])
def atualizar_moradia(id):
    try:
        moradia = MoradiaService.atualizar(id, request.get_json())
    except ValidacaoErro as erro:
        return jsonify({"erro": str(erro)}), 400
    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404
    return jsonify(moradia)