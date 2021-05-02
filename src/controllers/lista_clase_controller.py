from src.models.estudiantes_espacios_academicos import ListaClaseModel
from src.dto.lista_clase_dto import ListaClaseDTO

class ListaClaseController():
    def create(self, listaClaseDto:ListaClaseDTO):
        ListaClaseModel().add_estudiante_espacio(listaClaseDto)

    def delete(self, listaClaseDto:ListaClaseDTO):
        ListaClaseModel().delete_estudiante_espacio(listaClaseDto)

