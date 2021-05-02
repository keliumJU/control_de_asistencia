class EstudiantesDTO():
    identificacion:str
    nombres:str
    apellidos:str
    celular:str
    correo:str
    def __init__(self,identificacion,nombres,apellidos,celular,correo):
        self.identificacion=identificacion
        self.nombres=nombres
        self.apellidos=apellidos
        self.celular=celular
        self.correo=correo

