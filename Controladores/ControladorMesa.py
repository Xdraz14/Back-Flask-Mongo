from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        print("Creando Controlador Mesa")
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    def show(self,id):
        laMesa=Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    def update(self,id,infoMesa):
        mesaActual=Mesa(self.repositorioMesa.findById(id))
        mesaActual.num_Mesa=infoMesa["num_Mesa"]
        mesaActual.cant_Ced = infoMesa["cant_Ced"]
        mesaActual.info_Mesa = infoMesa["info_Mesa"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)