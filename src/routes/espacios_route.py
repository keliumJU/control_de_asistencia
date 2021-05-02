from src import app
from flask import render_template, request, redirect, url_for
#importar los controladores
from src.controllers.espacios_controller import EspaciosController
from src.controllers.semestres_controller import SemestresController

#importar los dto
from src.dto.espacios_dto import EspaciosDTO
from src.dto.semestres_dto import SemestresDTO


#crear los objetos globales
espaciosController = EspaciosController()
semestresController = SemestresController()

@app.route('/listar-espacios')
def listar_espacios():
    espacios=espaciosController.list()
    semestres=semestresController.list()
    return render_template('espacios/listar_espacios.html',espacios=espacios, semestres=semestres)

@app.route('/crear-espacio',methods=['POST'])
def crear_espacio():
    if request.method=='POST':
        nombre=request.form["nombre"]
        id_semestre=request.form["semestre"]
        
        print("------------------------->  "+str(id_semestre)+"  ---------------------------------<")

        semestre=semestresController.get(id_semestre)

        espacioDto=EspaciosDTO(
            nombre=nombre,
            semestre=semestre
        )

        espaciosController.create(espacioDto)
        return redirect(url_for('listar_espacios'))
    
@app.route('/editar-espacio', methods=['POST'])
def editar_espacio():
    if request.method=='POST':
        espacio_id=request.form["id"]
        nombre=request.form["nombre"]
        id_semestre=request.form["semestre"]

        semestre=semestresController.get(id_semestre)
        espacioDto=EspaciosDTO(
            nombre=nombre,
            semestre=semestre
        )
        espaciosController.update(espacioDto,espacio_id)
        return redirect(url_for('listar_espacios'))

@app.route('/borrar-espacio',methods=['POST'])
def borrar_espacio():
    if request.method=='POST':
        espacio_id=request.form["id"]
        espaciosController.delete(espacio_id)
        return redirect(url_for('listar_espacios'))


