from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cadena_conexion = 'mysql+mysqlconnector://root:@localhost:3306/bibioteca'
motordb = create_engine(cadena_conexion)
Session = sessionmaker(bind=motordb)
