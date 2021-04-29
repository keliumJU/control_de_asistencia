from src.config.settings import db
from src.models.sesiones import Sesiones

class EspaciosAcademicos(db.Model):
    __tablename__ = 'espacios_academicos'
    espacio_id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    #semestre=db.Column(db.Integer, nullable=False)
    semestre_id=db.Column(db.Integer,db.ForeignKey('semestres.semestre_id'))
    sesiones=db.relationship('Sesiones', backref='espacioSesion')    