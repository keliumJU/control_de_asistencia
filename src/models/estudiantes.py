from src.config.settings import db
from src.models.estudiantes_espacios_academicos import RegistroEspacioAcademico
from src.models.espacios_academicos import *
class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'
    identificacion=db.Column(db.String(10), primary_key=True, autoincrement=False)
    nombres=db.Column(db.String(255), default="est", nullable=False)
    apellidos=db.Column(db.String(255), default="ape" ,nullable=False)
    celular=db.Column(db.String(255),default="123", nullable=False)
    correo=db.Column(db.String(255), default="est@gamil.com", nullable=False)
    espacios_academicos=db.relationship('EspaciosAcademicos',secondary=RegistroEspacioAcademico,backref=db.backref('espacios'),lazy='dynamic')
    #id_espacio_academico=db.Column(db.String(255), nullable=False)
