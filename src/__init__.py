from flask import Flask, render_template

app = Flask(__name__, static_url_path = "/static", static_folder = "static", template_folder='views')

app.config.from_mapping(
    SECRET_KEY='dev',
)

#from src.controllers import estudiantes_controller
from src.routes import home 
from src.routes import estudiantes_route
from src.routes import espacios_route
from src.routes import lista_clase_route
from src.routes import sesiones_route
from src.routes import asistencia_route

from src.models.Modelos import *
def create_app():
    app.run(debug=True, port=3000)
