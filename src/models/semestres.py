from src.config.settings import db
from src.models.espacios_academicos import EspaciosAcademicos

class Semestres(db.Model):
    __tablename__='semestres'
    semestre_id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(25),nullable=False)
    espacio_academico=db.relationship('EspaciosAcademicos', backref='espacioSemestre')    