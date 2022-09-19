from flask import jsonify, Blueprint, request
from Controladores.ControladorRegistro import ControladorRegistro

controladorResultado = ControladorRegistro()

registro = Blueprint('registro', __name__)

'''Metodos para registrar resultados con sus respectivos decoradores'''


@registro.route("/resultado", methods=['GET'])
def getResultados():
    json = controladorResultado.index()
    return jsonify(json)


@registro.route("/resultado/candidato/<string:id_candidato>/mesa/<string:id_mesa>/partido/<string:id_partido>", methods=['POST'])
def crearResultado(id_candidato, id_mesa, id_partido):
    data = request.get_json()
    json = controladorResultado.create(data, id_candidato, id_mesa, id_partido)
    return jsonify(json)


@registro.route("/resultado/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def modificarResultado(id_resultado, id_candidato, id_mesa ):
    json = controladorResultado.update(id_resultado, id_candidato, id_mesa)
    return jsonify(json)


@registro.route("/resultado/<string:id>", methods=['GET'])
def getResultado(id):
    data = request.get_json()
    json = controladorResultado.show(id)
    return jsonify(json)

@registro.route("/resultado/<string:id>",methods=['DELETE'])
def eliminarRegistro(id):
    json = controladorResultado.delete(id)
    return jsonify(json)

@registro.route("/resultado/mesa/<string:id_mesa>", methods=['GET'])
def registrosEnMesa(id_mesa):
    json = controladorResultado.listarCandidatoEnMesa(id_mesa)
    return jsonify(json)

@registro.route("/resultado/suma/mesa", methods=['GET'])
def getSumaVotosTotalMesa():
    json = controladorResultado.sumaVotosEnMesa()
    return jsonify(json)

@registro.route("/resultado/suma/candidatoTotal", methods=['GET'])
def getSumaVotosTotalCandidato():
    json = controladorResultado.sumaVotosPorCandidatoMesas()
    return jsonify(json)
@registro.route("/resultado/suma/mesa/<string:id_mesa>", methods=['GET'])
def getSumaVotosCandidatoMesaEspecifica(id_mesa):
    json = controladorResultado.sumaVotosCandidatoMesaEspecifica(id_mesa)
    return jsonify(json)

@registro.route("/resultado/partidos/votos", methods=['GET'])
def getSumaVotosPartido():
    json = controladorResultado.sumaVotosPartido()
    return jsonify(json)