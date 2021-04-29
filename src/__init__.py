from flask import Flask, render_template

app = Flask(__name__, static_url_path = "/static", static_folder = "static", template_folder='views')


from src.controllers import *
from src.models import espacios_academicos 
from src.models import estudiantes 
from src.models import estudiantes_espacios_academicos 
from src.models import sesiones 
from src.models import asistencia
from src.models import semestres
def create_app():
    app.run(debug=True, port=5000)
