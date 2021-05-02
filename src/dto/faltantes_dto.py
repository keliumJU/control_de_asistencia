from src.models.Modelos import Sesiones, EspaciosAcademicos

class FaltantesDTO():
    sesion:Sesiones
    espacio:EspaciosAcademicos

    def __init__(self,sesion,espacio):
        self.sesion=sesion
        self.espacio=espacio