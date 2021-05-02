from src.config.settings import db

RegistroEspacioAcademico=db.Table('espacios_academicos_estudiante',
    db.Column('identificacion', db.String(10), db.ForeignKey('estudiantes.identificacion')),
    db.Column('id_espacio', db.Integer, db.ForeignKey('espacios_academicos.espacio_id'))
)

RegistroAsistencia=db.Table('asistencia',
    db.Column('identificacion', db.String(10), db.ForeignKey('estudiantes.identificacion')),
    db.Column('sesion_id', db.Integer, db.ForeignKey('sesiones.sesion_id'))
)

class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'
    identificacion=db.Column(db.String(10), primary_key=True, autoincrement=False)
    nombres=db.Column(db.String(255), default="est", nullable=False)
    apellidos=db.Column(db.String(255), default="ape" ,nullable=False)
    celular=db.Column(db.String(255),default="123", nullable=False)
    correo=db.Column(db.String(255), default="est@gamil.com", nullable=False)
    espacios_academicos=db.relationship('EspaciosAcademicos',enable_typechecks=False, secondary=RegistroEspacioAcademico,backref=db.backref('espacios'),lazy='dynamic')
    session=db.relationship('Sesiones',enable_typechecks=False,secondary=RegistroAsistencia,backref=db.backref('asistencia'),lazy='dynamic')
    #id_espacio_academico=db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'estudiantes',
        'with_polymorphic': '*'
    } 
class EspaciosAcademicos(db.Model):
    __tablename__ = 'espacios_academicos'
    espacio_id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    #semestre=db.Column(db.Integer, nullable=False)
    semestre_id=db.Column(db.Integer,db.ForeignKey('semestres.semestre_id'))
    sesiones_=db.relationship('Sesiones', enable_typechecks=False, backref='espacioSesion')    
    __mapper_args__ = {
        'polymorphic_identity': 'espacios_academicos',
        'with_polymorphic': '*'
    }

class Semestres(db.Model):
    __tablename__='semestres'
    semestre_id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(25),nullable=False)
    espacio_academico=db.relationship('EspaciosAcademicos', enable_typechecks=False, backref='espacioSemestre')    
    __mapper_args__ = {
        'polymorphic_identity': 'semestres',
        'with_polymorphic': '*'
    }


class Sesiones(db.Model):
    __tablename__ = 'sesiones'
    sesion_id=db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.Date,nullable=False)
    hora_ini=db.Column(db.Time,nullable=False)
    hora_fin=db.Column(db.Time,nullable=False)
    espacio_academico_id=db.Column(db.Integer,db.ForeignKey('espacios_academicos.espacio_id'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'sesiones',
        'with_polymorphic': '*'
    }
