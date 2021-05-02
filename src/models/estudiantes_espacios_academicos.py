from src.models.Modelos import EspaciosAcademicos, Estudiantes, db  
from src.dto.lista_clase_dto import ListaClaseDTO

class ListaClaseModel():
    def add_estudiante_espacio(self,listaClaseDto:ListaClaseDTO):
        listaClaseDto.espaciosAcademicos.espacios.append(listaClaseDto.estudiantes)
        db.session.commit()
    
    def delete_estudiante_espacio(self, listaClaseDto:ListaClaseDTO):
        #EspaciosAcademicos.query.filter_by(espacios=estudiante).delete()
        #chat.query.join(user.chats).filter(user.id == 1).all()
        listaClaseDto.espaciosAcademicos.espacios.remove(listaClaseDto.estudiantes)
        db.session.commit()
