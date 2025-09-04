from modelos.comuna import Comuna
from ORM.data.conexion import Session
from sqlalchemy import func

sesion = Session()

listado_comunas =sesion.query(Comuna).all()
if len (listado_comunas) >0:
    for comuna in listado_comunas:
        print(f'{comuna.id_comuna}, {comuna.codigo_comuna}, {comuna.nombre_comuna}')
else:
    print ("no ay comunas")