from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Registro import Registro
from bson import ObjectId

class RepositorioRegistro(InterfaceRepositorio[Registro]):
    def getListadoVotosCandidatoEnMesa(self, id_Mesa):
        theQuery = {"mesa.$id": ObjectId(id_Mesa)}
        return self.query(theQuery)
    def getMayorNotaPorCurso(self):
        query1={
                "$group": {
                    "_id": "$materia",
                    "max": {
                        "$max": "$nota_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioNotasEnMateria(self,id_materia):
        query1 = {
          "$match": {"materia.$id": ObjectId(id_materia)}
        }
        query2 = {
          "$group": {
            "_id": "$materia",
            "promedio": {
              "$avg": "$nota_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)