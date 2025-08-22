from Segundo_Semestre.modelos.nacionalidad import Nacionalidad


class Autor (Nacionalidad):
    def __init__(self,id_autor, nombre_autor, pseudonimo, id_nacionalidad, bio):
        super().__init__