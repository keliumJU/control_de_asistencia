from src import app
from flask import render_template,request,redirect,url_for

from src.controllers.lista_clase_controller import ListaClaseController
from src.controllers.espacios_controller import EspaciosController
from src.controllers.estudiantes_controller import EstudiantesController

from src.dto.lista_clase_dto import ListaClaseDTO

listaClaseController=ListaClaseController()
espaciosController=EspaciosController()
estudiantesController=EstudiantesController()

#esto deberia estar en una clase tambien?
@app.route('/listar-lista-clase')
def listar_lista_clase():
    espacios=espaciosController.list()
    students=estudiantesController.list()
    return render_template('lista_clase/lista_de_clase.html',espacios=espacios,students=students)

@app.route('/guardar-lista-clase',methods=['POST'])
def guardar_lista_clase():
    if request.method=='POST':
        id_espacio=request.form["id_espacio"]
        id_estudiante=request.form["id_estudiante"]

        print(id_espacio)
        print(id_estudiante)

        estudiante=estudiantesController.get(id_estudiante)
        espacio=espaciosController.get(id_espacio)

        listaClaseDto=ListaClaseDTO(
            espaciosAcademicos=espacio,
            estudiantes=estudiante
        )

        listaClaseController.create(listaClaseDto)

        return redirect(url_for('listar_lista_clase'))


@app.route('/borrar-lista-clase',methods=["POST"])
def borrar_lista_clase():
    if request.method=='POST':
        identificacion=request.form["id"]
        id_espacio=request.form["id_espacio"]

        estudiante=estudiantesController.get(identificacion)
        espacio=espaciosController.get(id_espacio)

        listaClaseDto=ListaClaseDTO(
            espaciosAcademicos=espacio,
            estudiantes=estudiante
        )

        listaClaseController.delete(listaClaseDto)

        return redirect(url_for('listar_lista_clase'))