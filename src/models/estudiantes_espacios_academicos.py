from src.config.settings import db

RegistroEspacioAcademico=db.Table('espacios_academicos_estudiante',
    db.Column('identificacion', db.String(10), db.ForeignKey('estudiantes.identificacion')),
    db.Column('id_espacio', db.Integer, db.ForeignKey('espacios_academicos.espacio_id'))
)

