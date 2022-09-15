from flask import jsonify, Blueprint


# metodos de prueba de conexion

registraduria = Blueprint('registraduria', __name__)
@registraduria.route("/", methods=['GET'])  # El decorador “@app.route” es necesario para que flask detecte que se está declarando un servicio
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

