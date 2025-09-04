from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cadena_conexion = 'mysql+mysqlconector://root:@localhost:3306/centro_libros'
motordb = create_engine(cadena_conexion)
Session = sessionmaker(bind=motordb)

