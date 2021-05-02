from src.models.espacios_academicos import EspaciosAcademicosModel
from src.dto.espacios_dto import EspaciosDTO


class EspaciosController():
    def create(self,espaciosDto:EspaciosDTO):
        EspaciosAcademicosModel().add_espacio(espaciosDto)
        
    def list(self):
        return EspaciosAcademicosModel().list_espacios()

    def get(self,id_):
        return EspaciosAcademicosModel().get_espacio(id_)

    def update(self, espaciosDto:EspaciosDTO, id_):
        EspaciosAcademicosModel().update_espacio(espaciosDto, id_)

    def delete(self, id_):
        EspaciosAcademicosModel().delete_espacio(id_)
