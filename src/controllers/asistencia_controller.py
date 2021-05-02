from src.models.asistencia import AsistenciaModel
from src.dto.asistencia_dto import AsistenciaDTO
from src.dto.faltantes_dto import FaltantesDTO

class AsistenciaController():
    def create(self, asistenciaDto:AsistenciaDTO):
        AsistenciaModel().add_asistencia(asistenciaDto)
    
    def listar_estudiantes_faltantes(self, faltantesDto:FaltantesDTO):
        return AsistenciaModel().listar_faltantes(faltantesDto)
    
