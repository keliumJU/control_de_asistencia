from src.dto.asistencia_dto import AsistenciaDTO
from src.config.settings import db
from src.dto.faltantes_dto import FaltantesDTO

from src.models.estudiantes import EstudiantesModel

class AsistenciaModel():
    def add_asistencia(self,asistenciaDto:AsistenciaDTO):
        asistenciaDto.sesion.asistencia.append(asistenciaDto.estudiante)
        db.session.commit()
    
    def listar_faltantes(self,faltantesDto:FaltantesDTO):
        #verificar los estudiantes que no asistieron
        #vamos a realizar la busqueda por identificacion
        lista_ids=[]
        for iden in faltantesDto.espacio.espacios:
            lista_ids.append(int(iden.identificacion))

        lista_ids_asis=[] 
        for iden in faltantesDto.sesion.asistencia:
            lista_ids_asis.append(int(iden.identificacion))

        lista_ids.sort()
        lista_ids_asis.sort()

        sz=len(lista_ids_asis)
        print("tamanio")
        print(sz)
        print("lista ids normal")
        print(lista_ids)
        print("lista_ids asis")
        print(lista_ids_asis)
        #[1234]
        #[1111,1234,1007403404]
        for i in range(len(lista_ids_asis)):
            for j in range(len(lista_ids)):
                if(lista_ids_asis[i]==lista_ids[j]):
                    lista_ids[j]=-1


        #dejamos la lista limpia
        ids_faltantes=[]
        for i in range(len(lista_ids)):
            if(lista_ids[i]!=-1):
                ids_faltantes.append(lista_ids[i])

        #buscamos los estudiantes faltantes en la db y los retornamos 
        estudiantes_faltantes=[]
        print("ESTOS SON LOS IDS FALTANTES *****")
        print(ids_faltantes)
        for i in range(len(ids_faltantes)):
            estudiantesModel=EstudiantesModel().get_estudiante(ids_faltantes[i])
            estudiantes_faltantes.append(estudiantesModel)

        return estudiantes_faltantes





