#from src.config.settings import db
from src.dto.estudiantes_dto import EstudiantesDTO
from src.models.Modelos import Estudiantes, db 
from src.dto.sesion_estudiantes_dto import SesionEstudiantesDTO
class EstudiantesModel(Estudiantes):
    def json(self):
        return {
            'identificacion':self.identificacion,
            'nombres':self.nombres,
            'apellidos':self.apellidos,
            'celular':self.celular,
            'correo':self.correo,
        }
    def add_estudiante(self, estudianteDto:EstudiantesDTO):
        estudiante=EstudiantesModel(identificacion=estudianteDto.identificacion,
                                nombres=estudianteDto.nombres,
                                apellidos=estudianteDto.apellidos,
                                celular=estudianteDto.celular,
                                correo=estudianteDto.correo,
                                )
        db.session.add(estudiante)
        db.session.commit()
    
    def listar_estudiantes(self):
        return EstudiantesModel.query.all()

    def get_estudiante(self, id_):
        return Estudiantes.query.filter_by(identificacion=id_).first()

    def update_estudiante(self, estudianteDto:EstudiantesDTO):
        estudiante=EstudiantesModel.query.filter_by(identificacion=estudianteDto.identificacion).first()
        estudiante.nombres=estudianteDto.nombres
        estudiante.apellidos=estudianteDto.apellidos
        estudiante.celular=estudianteDto.celular
        estudiante.correo=estudianteDto.correo
        db.session.commit() 
    
    def delete_estudiante(self, _id):
        EstudiantesModel.query.filter_by(identificacion=_id).delete()
        db.session.commit()
    
    def add_to_sesion(self, sesionEstudiantesDto:SesionEstudiantesDTO):

        for estudiante in sesionEstudiantesDto.lista_estudiantes:
            sesionEstudiantesDto.sesion.asistencia.append(estudiante)

        db.session.commit()
