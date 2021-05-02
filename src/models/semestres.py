from src.models.Modelos import Semestres,db
from src.dto.semestres_dto import SemestresDTO
from src.dto.espacios_dto import EspaciosDTO

class SemestresModel(Semestres):
    def json(self):
        return {
            'semestre_id':self.semestre_id,
            'nombre':self.nombre
        }

    def list_semestre(self):
        return SemestresModel.query.all()

    def get_semestre(self,id_):
        return Semestres.query.filter_by(semestre_id=id_).first()