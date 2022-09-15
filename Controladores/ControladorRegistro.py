from Modelos.Registro import Registro
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioRegistro import RepositorioRegistro
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorRegistro():
    def __init__(self):
        self.repositorioRegistro = RepositorioRegistro()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioRegistro.findAll()

    """
    Asignacion candidato y mesa a registro
    """

    def create(self, infoRegistro, id_candidato, id_mesa):
        nuevoRegistro = Registro(infoRegistro)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoRegistro.candidato = elCandidato
        nuevoRegistro.mesa = laMesa
        return self.repositorioRegistro.save(nuevoRegistro)

    def show(self, id):
        elRegistro = Registro(self.repositorioRegistro.findById(id))
        return elRegistro.__dict__

    """
    Modificación de inscripción (estudiante y materia)
    """

    def update(self, id, infoRegistro, id_candidato, id_mesa):
        elRegistro = Registro(self.repositorioRegistro.findById(id))
        elRegistro.numVotos = infoRegistro["numVotos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elRegistro.candidato = elCandidato
        elRegistro.materia = laMesa
        return self.repositorioRegistro.save(elRegistro)

    def delete(self, id):
        return self.repositorioRegistro.delete(id)

    "Obtener todos los inscritos en una materia"

    def listarInscritosEnMateria(self, id_materia):
        return self.repositorioRegistro.getListadoInscritosEnMateria(id_materia)

    "Obtener notas mas altas por curso"

    def notasMasAltasPorCurso(self):
        return self.repositorioRegistro.getMayorNotaPorCurso()

    "Obtener promedio de notas en materia"

    def promedioNotasEnMateria(self, id_materia):
        return self.repositorioRegistro.promedioNotasEnMateria(id_materia)
