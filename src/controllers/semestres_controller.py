from src.models.semestres import SemestresModel

class SemestresController():
    def list(self):
        return SemestresModel().list_semestre()
    
    def get(self, id_):
        return SemestresModel().get_semestre(id_)