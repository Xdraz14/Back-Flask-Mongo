from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Registro import Registro
from bson import ObjectId

class RepositorioRegistro(InterfaceRepositorio[Registro]):
    def getListadoVotosCandidatoEnMesa(self, id_Mesa):
        theQuery = {"mesa.$id": ObjectId(id_Mesa)}
        return self.query(theQuery)

    def sumaVotosCandidatoMesaEspecifica(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "Suma_Voto_Candidado_En_Mesa": {
                    "$sum": "$numVotos"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def sumaVotosPorCandidatoMesas(self):
        query2 = {
            "$group": {
                "_id": "$candidato",
                "suma_votos_candidato": {
                    "$sum": "$numVotos"
                }
            }
        }
        pipeline = [query2]
        return self.queryAggregation(pipeline)
    def sumaVotosEnMesa(self):
        query2 = {
            "$group": {
                "_id": "$mesa",
                "suma_votos_mesa": {
                    "$sum": "$numVotos"
                }
            }
        }
        pipeline = [query2]
        return self.queryAggregation(pipeline)

    def sumaVotosPartido(self):
        #query1 = {
         #   "$match": {"partido.$id": ObjectId(id_partido)}
       # }
        query2 = {
            "$group": {
                "_id": "$partido",
                "Suma_Voto_partido": {
                    "$sum": "$numVotos"
                }
            }
        }
        pipeline = [query2]
        return self.queryAggregation(pipeline)


