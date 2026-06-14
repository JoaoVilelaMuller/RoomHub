from flask import Blueprint, jsonify, request
from dao.moradia_dao import MoradiaDAO
from models.moradia import Moradia



moradia_bp = Blueprint("moradias", __name__)



@moradia_bp.route("/api/moradias", methods=["GET"])
def listar_moradias():
    return jsonify([m.__dict__ for m in MoradiaDAO.listar()])



@moradia_bp.route("/api/moradias/<int:id>", methods=["GET"])
def buscar_moradia(id):
    moradia = MoradiaDAO.buscar_por_id(id)

    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404

    return jsonify(moradia.__dict__)



@moradia_bp.route("/api/moradias", methods=["POST"])
def criar_moradia():
    dados = request.get_json()

    moradia = Moradia(
        dados["id"],
        dados["titulo"],
        dados["descricao"],
        dados["cidade"],
        dados["universidade"],
        dados["preco"]
    )

    MoradiaDAO.adicionar(moradia)

    return jsonify(moradia.__dict__), 201



@moradia_bp.route("/api/moradias/<int:id>", methods=["DELETE"])
def excluir_moradia(id):
    moradia = MoradiaDAO.remover(id)

    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404

    return jsonify(moradia.__dict__)



@moradia_bp.route("/api/moradias/<int:id>", methods=["PUT"])
def atualizar_moradia(id):

    dados = request.get_json()

    moradia = MoradiaDAO.atualizar(id, dados)

    if moradia is None:
        return jsonify({"erro": "Moradia não encontrada"}), 404

    return jsonify(moradia.__dict__)