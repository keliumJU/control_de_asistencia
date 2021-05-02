from src.models.Modelos import EspaciosAcademicos,db
from src.dto.semestres_dto import SemestresDTO
from src.dto.espacios_dto import EspaciosDTO


class EspaciosAcademicosModel(EspaciosAcademicos):

    def list_espacios(self):
        return EspaciosAcademicosModel.query.all()

    def get_espacio(self, id_):
        return EspaciosAcademicos.query.filter_by(espacio_id=id_).first()
    
    def add_espacio(self, espacioDto:EspaciosDTO):
        espacio=EspaciosAcademicos(
            nombre=espacioDto.nombre,
            espacioSemestre=espacioDto.semestre
        )
        db.session.add(espacio)
        db.session.commit()
    
    def update_espacio(self, espacioDto:EspaciosDTO, id_):
        espacio=EspaciosAcademicos.query.filter_by(espacio_id=id_).first()
        espacio.nombre=espacioDto.nombre
        espacio.espacioSemestre=espacioDto.semestre
        db.session.commit()
    
    def delete_espacio(self, id_):
        EspaciosAcademicosModel.query.filter_by(espacio_id=id_).delete()
        db.session.commit()