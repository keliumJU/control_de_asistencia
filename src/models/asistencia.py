from src.config.settings import db

RegistroAsistencia=db.Table('asistencia',
    db.Column('identificacion', db.String(10), db.ForeignKey('estudiantes.identificacion')),
    db.Column('sesion_id', db.Integer, db.ForeignKey('sesiones.sesion_id'))
)


