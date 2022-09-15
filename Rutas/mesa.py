from flask import jsonify, Blueprint,request
from Controladores.ControladorMesa import ControladorMesa

miControladorMesa = ControladorMesa()

mesa = Blueprint('mesa', __name__)

'''Metodos para registrar mesa con sus respectivos decoradores'''


@mesa.route("/mesa", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)


@mesa.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)


@mesa.route("/mesa/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


@mesa.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@mesa.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)
