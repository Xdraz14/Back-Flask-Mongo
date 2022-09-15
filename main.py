import json
from flask import Flask
from flask_cors import CORS
from waitress import serve
from Rutas.registraduria import registraduria
from Rutas.mesa import mesa
from Rutas.partido import partido
from Rutas.candidato import candidato
from Rutas.registro import registro

'''Lee el archivo para del cofig para las configuraciones del puerto'''
app = Flask(__name__)
cors = CORS(app)

def loadFileConfig():
    with open('config.json') as f:  # método leer el archivo de configuración del proyecto
        data = json.load(f)
    return data

app.register_blueprint(registraduria)
app.register_blueprint(mesa)
app.register_blueprint(partido)
app.register_blueprint(candidato)
app.register_blueprint(registro)

# Metodo Main
if __name__ == '__main__':
    dataConfig = loadFileConfig()  # se carga el archivo config.json
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    '''se crea la instancia del servidor con la url del backend y puerto especificado en el archivo de configuración.'''
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
    print(dataConfig["password"])
