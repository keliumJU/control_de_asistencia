from src import app
from flask import render_template,request,redirect,url_for

from src.controllers.sesiones_controller import SesionesController, SesionesDTO
from src.controllers.espacios_controller import EspaciosController, EspaciosDTO

import datetime
import time

sesionesController=SesionesController()
espaciosController=EspaciosController()


@app.route('/litar-sesiones')
def listar_sesiones():
    sesiones=sesionesController.list()
    espacios=espaciosController.list()
    return render_template('sesiones/listar_sesiones.html',sesiones=sesiones, espacios=espacios)

@app.route('/crear-sesion',methods=['POST'])
def crear_sesion():
    if request.method=='POST':
        fecha=request.form["fecha"]
        hora_ini=request.form["hora_ini"]
        hora_end=request.form["hora_end"]
        id_espacio=request.form["id_espacio"]

        espacio=espaciosController.get(id_espacio)

        sesionDto=SesionesDTO(
            fecha=fecha,
            hora_ini=hora_ini,
            hora_end=hora_end,
            espacios=espacio
        )

        sesionesController.create(sesionDto)

        return redirect(url_for('listar_sesiones'))



