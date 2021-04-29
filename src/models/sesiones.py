from src.config.settings import db
from src.models.asistencia import RegistroAsistencia
from src.models.estudiantes import Estudiantes
class Sesiones(db.Model):
    __tablename__ = 'sesiones'
    sesion_id=db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.Date,nullable=False)
    hora_ini=db.Column(db.Time,nullable=False)
    hora_fin=db.Column(db.Time,nullable=False)
    session=db.relationship('Estudiantes',secondary=RegistroAsistencia,backref=db.backref('asistencia'),lazy='dynamic')
    espacio_academico_id=db.Column(db.Integer,db.ForeignKey('espacios_academicos.espacio_id'))

