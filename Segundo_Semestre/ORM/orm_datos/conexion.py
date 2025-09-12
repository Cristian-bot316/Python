from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conexion = "mysql+mysqlconnector://root:@localhost:3306/bibbioteca"
motor_db = create_engine(conexion)
Session = sessionmaker(bind=motor_db)
