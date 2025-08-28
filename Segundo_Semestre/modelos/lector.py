class Lector(Biblioteca, Direccion):
    def __init__(self, id_lector, rut, digito_verificador, nombre_lector, id_biblioteca, telefono, correo, ID_direccion):
        self.rut = rut
        self.libros_prestados = libros_prestados
        self.telefono = telefono
        self.correo = correo
        self.id_direccion = id_direccion