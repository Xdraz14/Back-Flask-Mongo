from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Partido import Partido
from bson import ObjectId


class RepositorioPartido(InterfaceRepositorio[Partido]):
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

