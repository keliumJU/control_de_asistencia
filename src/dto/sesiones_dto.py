from src.models.Modelos import EspaciosAcademicos
import datetime
import time

class SesionesDTO():
    fecha:datetime
    hora_ini:time
    hora_end:time
    espacios:EspaciosAcademicos

    def __init__(self,fecha,hora_ini,hora_end,espacios):
        self.fecha=fecha
        self.hora_ini=hora_ini
        self.hora_end=hora_end
        self.espacios=espacios
