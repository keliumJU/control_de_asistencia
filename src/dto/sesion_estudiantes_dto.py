from src.models.Modelos import Sesiones

class SesionEstudiantesDTO():
    lista_estudiantes:list
    sesion:Sesiones

    def __init__(self,lista_estudiantes,sesion):
        self.lista_estudiantes=lista_estudiantes
        self.sesion=sesion
