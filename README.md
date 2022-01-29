# python_code
#INSTALAR
_PYTHON11.YA QUE ES LA VERSION MAS ESTABLE
_SQLPOSGRET
_VISUALSTUDIO CODE/SUBLIME

#PARA LA INSTALACION DE MODULOS PYTHON
pip install requests
pip install sqlalchemy

#importacion de modulo para descarga de archivos
import requests as req

#impor del orm para la coneccion de BD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

#URL MUSEOS
URL_MUSEOS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'

# DECLARACIONES DE VARIABLES PARA USO DE BASE DE DATOS
Base = declarative_base()
engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')


#DEFINICION DEL MODELO DE LA TABLA DE ESPACIOS PUBLICOS (MUSEOS, BIBLIOTECAS Y CINES)
class EspaciosPublicos(Base):
	__tablename__ = 'espacios_publicos'
	id = Column(Integer(), primary_key=True)
	cod_localidad = Column(Integer(), nullable=True, unique=False)
	id_provincia = Column(Integer(), nullable=True, unique=False)
	id_departamento = Column(Integer(), nullable=True, unique=False)
	created_at = Column(DateTime(), default=datetime.now())
	categoria = Column(String(50), nullable=True, unique=False)

def __str__(self):
	return self.username

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
	#Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

#RECORRER LOS MUSEOS
#realiza un req con el metodo get y deja el resul en la variable en rq
with req.get(URL_MUSEOS, stream=True) as rq:
	#CONTADOR DE LINEAS
	linenumber = 0
	#ITERAR SOBRE CADA LINEA
	for line in rq.iter_lines(delimiter=b'\n'):
		
		#SI NO ES LA PRIMERA LINEA (ESTO SE USA PARA NO TOMAR EN CUENTA LA PRIMERA LINEA DEL ARCHIVO)
		if linenumber != 0:
			linenumber += 1
			#la funcion str convierte una variable en un string
			strline = str(line)
			#la funcion string separa la variable strline usando el caracter ","
			list_fields = strline.split(',')
			print('list_fields[0]: ' + list_fields[0])
			
			#ELIMINA EL CARACTER DE INICIO DE LINEA EL CUAL ES <b>
			#SE USA CUANDO EL CARACTER INICIAL SE SEPARA POR UNA " [COMILLA DOBLE] DEL VALOR DEL PRIMER CAMPO ("B"NNNN")
			if  list_fields[0].find('\'') == -1:
				#si la comilla es simple
				id_departamentoList = list_fields[0].split('\"')
			#SE USA CUANDO EL CARACTER INICIAL SE SEPARA POR UNA ' [COMILLA SIMPLE] DEL VALOR DEL PRIMER CAMPO ("B"NNNN")
			else:
				id_departamentoList = list_fields[0].split('\'')
			
			#ASIGNAMOS EL VALOR NUMERICO DEL PRIMER CAMPO OBTENIDO
			id_departamento = id_departamentoList[1]
			#SI EL TAMAÑO DE LA LISTA DE CAMPOS ES MAYOR QUE UN MINIMO ENTONCES CREO UN OBJETO ESPACIO PUBLICO CON SUS VALORES CORRESPONDIENTES
			if len(list_fields) > 3:
				space1 = EspaciosPublicos(cod_localidad=list_fields[2], id_provincia=list_fields[1], id_departamento=id_departamento, categoria='MUSEO')
				session.add(space1)
		#SI ES LA PRIMERA LINEA
		else:
			linenumber += 1
	session.commit()
  
  
  #
#select categoria, count(id_space) from espacios_publicos group by categoria
#select fuente, count(id_space) from espacios_publicos group by fuente
#select provincia, count(id_space) from espacios_publicos group by provincia
