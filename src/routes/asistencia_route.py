from src import app
from flask import render_template,redirect,request,url_for,session

from src.controllers.espacios_controller import EspaciosController
from src.controllers.sesiones_controller import SesionesController
from src.controllers.estudiantes_controller import EstudiantesController
from src.controllers.asistencia_controller import AsistenciaController


from src.dto.sesion_estudiantes_dto import SesionEstudiantesDTO
from src.dto.faltantes_dto import FaltantesDTO

estudiantesController=EstudiantesController()
espaciosController=EspaciosController()
sesionesController=SesionesController()
asistenciaController=AsistenciaController()

@app.route('/listar-asistencia')
def listar_asistencia():
    sesiones=sesionesController.list()

    return render_template('asistencia/asistencia.html',sesiones=sesiones)


@app.route('/buscar-estudiantes',methods=['POST'])
def buscar_estudiantes():
    if request.method=='POST':
        id_sesion=request.form["id_sesion"]
        sesion=sesionesController.get(id_sesion)

        session["sesion_now"]=id_sesion

        espacio=espaciosController.get(sesion.espacioSesion.espacio_id)
        estudiantes=espacio.espacios
        sesiones=sesionesController.list()

        return render_template('asistencia/asistencia.html',sesiones=sesiones, estudiantes=estudiantes)


@app.route('/registro-asistencia',methods=['POST'])
def registro_asistencia():
    if request.method=='POST':
        #obtenemos la sesion por medio de la la variable global sesion_now
        sesion=sesionesController.get(session["sesion_now"])
        espacio=espaciosController.get(sesion.espacioSesion.espacio_id)

        #los id de los estudiantes que agregaremos a la tabla asistencia
        opciones=request.form.getlist("options")
        print("etos son los estudiantes que asistieron:")
        print(opciones)
        #lista_de_estudiantes que asistieron
        lista_estudiantes=estudiantesController.get_students_by_ids(opciones)
        print("LISTA DE ESTUDIANTES QUE ASISTIERON")
        print(lista_estudiantes)
        #dto para crear el objeto que registra los estudiantes que asistieron a una sesion
        sesionEstudiantesDto=SesionEstudiantesDTO(
            lista_estudiantes=lista_estudiantes,
            sesion=sesion
        )
        print("DTO LISTA ESTUDIANTES")
        print(sesionEstudiantesDto.lista_estudiantes)
        #registramos los estudiantes que asistieron a una sesion
        estudiantesController.add_to_sesion_student(sesionEstudiantesDto)
        print("lista sesion estudiantes asist") 
        print(sesion.asistencia)
        #Lista de estudiantes que faltaron a la sesion
        faltantes=FaltantesDTO(
            sesion=sesion,
            espacio=espacio
        )

        lista_estudiantes_faltantes=asistenciaController.listar_estudiantes_faltantes(faltantes)

        print(lista_estudiantes_faltantes)

        estudiantes=espacio.espacios
        sesiones=sesionesController.list()

        return render_template('asistencia/asistencia.html',faltantes=lista_estudiantes_faltantes,
                                estudiantes=estudiantes, sesiones=sesiones, sesionVar=sesion)
         #return redirect(url_for('listar_asistencia'))


