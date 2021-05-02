from src.models.Modelos import EspaciosAcademicos,Estudiantes

class ListaClaseDTO():
    espaciosAcademicos:EspaciosAcademicos
    estudiantes:Estudiantes

    def __init__(self,espaciosAcademicos,estudiantes):
        self.espaciosAcademicos=espaciosAcademicos
        self.estudiantes=estudiantes
    
