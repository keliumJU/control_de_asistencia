from src.models.sesiones import SesionesModel,SesionesDTO

class SesionesController():
    def list(self):
        return SesionesModel().listar_sesiones()
    
    def create(self,sesionesDto:SesionesDTO):
        SesionesModel().add_sesion(sesionesDto)

    def get(self, id_):
        return SesionesModel().get_sesion(id_)