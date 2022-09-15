from flask import jsonify, Blueprint,request
from Controladores.ControladorRegistro import ControladorRegistro

controladorResultado = ControladorRegistro()

registro = Blueprint('registro', __name__)

'''Metodos para registrar resultados con sus respectivos decoradores'''


@registro.route("/resultado", methods=['GET'])
def getResultados():
    json = controladorResultado.index()
    return jsonify(json)


@registro.route("/resultado", methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = controladorResultado.create(data)
    return jsonify(json)


@registro.route("/resultado/<int:id>", methods=['GET'])
def getResultado(id):
    json = controladorResultado.show(id)
    return jsonify(json)


@registro.route("/resultado/<int:id>", methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json = controladorResultado.update(id, data)
    return jsonify(json)
