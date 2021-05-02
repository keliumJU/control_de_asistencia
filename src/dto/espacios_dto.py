from src.models.Modelos import Semestres 

class EspaciosDTO():
    nombre:str
    semestre:Semestres

    def __init__(self,nombre,semestre):
        self.nombre=nombre
        self.semestre=semestre
