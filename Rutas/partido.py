from flask import jsonify, Blueprint,request
from Controladores.ControladorPartido import ControladorPartido

controladorPartido = ControladorPartido()

partido = Blueprint('partido', __name__)

'''Metodos para Partido con sus respectivos decoradores'''


@partido.route("/partido", methods=['GET'])
def getPartidos():
    json = controladorPartido.index()
    return jsonify(json)


@partido.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.create(data)
    return jsonify(json)


@partido.route("/partido/<int:id>", methods=['GET'])
def getPartido(id):
    json = controladorPartido.show(id)
    return jsonify(json)


@partido.route("/partido/<int:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)


@partido.route("/partido/<int:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.delete(id)
    return jsonify(json)
