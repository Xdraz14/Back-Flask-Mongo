from Modelos.Registro import Registro
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido
from Repositorios.RepositorioRegistro import RepositorioRegistro
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorRegistro():
    def __init__(self):
        self.repositorioRegistro = RepositorioRegistro()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()
        print("Creando Controlador Registro")

    def index(self):
        return self.repositorioRegistro.findAll()

    """
    Asignacion candidato y mesa a registro
    """

    def create(self, infoRegistro, id_candidato, id_mesa, id_partido):
        nuevoRegistro = Registro(infoRegistro)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elPartido = Partido(self.repositorioPartido.findById(id_partido))
        nuevoRegistro.partido = elPartido
        nuevoRegistro.candidato = elCandidato
        nuevoRegistro.mesa = laMesa
        return self.repositorioRegistro.save(nuevoRegistro)

    def show(self, id):
        elRegistro = Registro(self.repositorioRegistro.findById(id))
        return elRegistro.__dict__

    """
    Modificación de Registro (candidato y mesa)
    """

    def update(self, id, infoRegistro, id_candidato, id_mesa, id_partido):
        elRegistro = Registro(self.repositorioRegistro.findById(id))
        elRegistro.numVotos = infoRegistro["numVotos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elPartido = Partido(self.repositorioPartido.findById(id_partido))
        elRegistro.candidato = elCandidato
        elRegistro.mesa = laMesa
        elRegistro.partido = elPartido
        return self.repositorioRegistro.save(elRegistro)

    def delete(self, id):
        return self.repositorioRegistro.delete(id)


    "Obtener todos los candidatos votados en una mesa"

    def listarCandidatoEnMesa(self, id_mesa):
        return self.repositorioRegistro.getListadoVotosCandidatoEnMesa(id_mesa)

    "Obtener suma de votos total en mesa "
    def sumaVotosEnMesa(self):
        return self.repositorioRegistro.sumaVotosEnMesa()

    def sumaVotosCandidatoMesaEspecifica(self, id_mesa):
        return self.repositorioRegistro.sumaVotosCandidatoMesaEspecifica(id_mesa)

    def sumaVotosPorCandidatoMesas(self):
        return self.repositorioRegistro.sumaVotosPorCandidatoMesas()

    def sumaVotosPartido(self):
        return self.repositorioRegistro.sumaVotosPartido()

    '''

    "Obtener lasc mas altas por curso"

    def notasMasAltasPorCurso(self):
        return self.repositorioRegistro.getMayorNotaPorCurso()

    "Obtener promedio de notas en materia"

    def promedioNotasEnMateria(self, id_materia):
        return self.repositorioRegistro.promedioNotasEnMateria(id_materia)
'''