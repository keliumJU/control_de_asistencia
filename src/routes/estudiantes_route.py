from src import app
from src.controllers.estudiantes_controller import EstudiantesController 
from flask import render_template, request, redirect, url_for, session
from src.dto.estudiantes_dto import EstudiantesDTO 

#objeto para acceder a los metodos del controlador
estudianteController=EstudiantesController()

@app.route('/crear-estudiante', methods=['POST'])
def crear_estudiante():
    if request.method=='POST':
        identificacion=request.form["identificacion"]
        nombres=request.form["nombres"]
        apellidos=request.form["apellidos"]
        celular=request.form["celular"]
        correo=request.form["correo"]

        estudianteDto=EstudiantesDTO(
            identificacion=identificacion,
            nombres=nombres,
            apellidos=apellidos,
            celular=celular,
            correo=correo
        )
        #print("some------------>"+str(estudianteDto))
        estudianteController.create(estudianteDto)
        return redirect(url_for('listar_estudiantes'))

@app.route('/listar-estudiantes')
def listar_estudiantes():
    estudiantes=estudianteController.list()
    print(estudiantes)
    return render_template('estudiantes/listar_estudiantes.html',estudiantes=estudiantes)


@app.route('/guardar-estudiante', methods=['POST'])
def guardar_estudiante():
    if request.method=='POST':
        identificacion=request.form["identificacion"]
        nombres=request.form["nombres"]
        apellidos=request.form["apellidos"]
        celular=request.form["celular"]
        correo=request.form["correo"]

        estudianteDto=EstudiantesDTO(
            identificacion=identificacion,
            nombres=nombres,
            apellidos=apellidos,
            celular=celular,
            correo=correo
        )

        estudianteController.update(estudianteDto)
        return redirect(url_for('listar_estudiantes'))

@app.route('/borrar-estudiante',methods=['POST'])
def borrar_estudiante():
    if request.method=='POST':
        identificacion=request.form["identificacion"]
        estudianteController.delete(identificacion)
        return redirect(url_for('listar_estudiantes'))
