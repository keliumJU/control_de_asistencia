from src.models.estudiantes import EstudiantesModel
from src.dto.estudiantes_dto import EstudiantesDTO
from src.dto.sesion_estudiantes_dto import SesionEstudiantesDTO

class EstudiantesController():
    def create(self,estudianteDto:EstudiantesDTO):
        EstudiantesModel().add_estudiante(estudianteDto)

    def list(self):
        return EstudiantesModel().listar_estudiantes()

    def get(self,id_):
        return EstudiantesModel().get_estudiante(id_)

    def update(self,estudianteDto:EstudiantesDTO):
        EstudiantesModel().update_estudiante(estudianteDto)

    def delete(self, _id):
        EstudiantesModel().delete_estudiante(_id)
    
    def add_to_sesion_student(self, sesionEstudiantesDto:SesionEstudiantesDTO):
        EstudiantesModel().add_to_sesion(sesionEstudiantesDto)

    def get_students_by_ids(self, list_ids):
        lista_estudiantes=[]
        for i in range(len(list_ids)):
            lista_estudiantes.append(EstudiantesModel().get_estudiante(int(list_ids[i])))
        return lista_estudiantes
