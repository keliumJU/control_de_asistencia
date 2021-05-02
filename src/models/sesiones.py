from src.models.Modelos import Sesiones,db
from src.dto.sesiones_dto import SesionesDTO
class SesionesModel():
    def add_sesion(self,sesionesDto:SesionesDTO):
        sesion=Sesiones(
            fecha=sesionesDto.fecha,
            hora_ini=sesionesDto.hora_ini,
            hora_fin=sesionesDto.hora_end,
            espacioSesion=sesionesDto.espacios
        )
        db.session.add(sesion)
        db.session.commit()
    
    def listar_sesiones(self):
        return Sesiones.query.all()

    def get_sesion(self, id_):
        return Sesiones.query.filter_by(sesion_id=id_).first()
        
    def update_sesiones(self):
        pass

    def delete_sesiones(self):
        pass