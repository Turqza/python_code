#Import download
import requests as req

#Import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

#URL MUSEOS
URL_MUSEOS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'

URL_CINES = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'

URL_BIBLIOTECAS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'

# DECLARACIONES DE VARIABLES PARA USO DE BASE DE DATOS
Base = declarative_base()
engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')


#DEFINICION DEL MODELO DE LA TABLA DE ESPACIOS PUBLICOS (MUSEOS, BIBLIOTECAS Y CINES)
class EspaciosPublicos(Base):
	__tablename__ = 'espacios_publicos'
	id_space = Column(Integer(), primary_key=True)
	cod_localidad = Column(Integer(), nullable=True, unique=False)
	id_provincia = Column(Integer(), nullable=True, unique=False)
	id_departamento = Column(Integer(), nullable=True, unique=False)
	created_at = Column(DateTime(), default=datetime.now())
	categoria = Column(String(50), nullable=True, unique=False)
	record_type = Column(String(50), nullable=True, unique=False)
	provincia = Column(String(50), nullable=True, unique=False)
	localidad = Column(String(200), nullable=True, unique=False)
	nombre = Column(String(200), nullable=True, unique=False)
	codigo_postal = Column(String(200), nullable=True, unique=False)
	telefono = Column(String(200), nullable=True, unique=False)
	email = Column(String(200), nullable=True, unique=False)
	web = Column(String(200), nullable=True, unique=False)
	fuente = Column(String(200), nullable=True, unique=False)


class ResumenCines(Base):
	__tablename__ = 'resumen_cines'
	id_cine = Column(Integer(), primary_key=True)
	cantidad_pantallas = Column(Integer(), nullable=True, unique=False)
	cantidad_butacas = Column(Integer(), nullable=True, unique=False)
	cantidad_de_espacios_incaa = Column(Integer(), nullable=True, unique=False)
	created_at = Column(DateTime(), default=datetime.now())
	
	#inconsistencia de datos del arch defines

def __str__(self):
	return self.username

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
	#Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

def normalize(s):
    replacements = (
        ("\\xc3\\xa1", "a"),
        ("\\xc3\\xa9", "e"),
        ("\\xc3\\xad", "i"),
        ("\\xc3\\xb3", "o"),
        ("\\xc3\\xba", "u"),
        ("\\xc3\\xb1", "ñ"),
        ("\\xc2\\xa0", ""),
        ("\\xc3\\x89", "e"),
        ("\\xc2\\xb0", "°"),
        
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def Iiterate_Spaces(URL_SPACES, session, record_type_name):
	#RECORRER LOS MUSEOS
	with req.get(URL_SPACES, stream=True) as rq:
		#CONTADOR DE LINEAS
		linenumber = 0
		#ITERAR SOBRE CADA LINEA
		for line in rq.iter_lines(delimiter=b'\n'):
			
			#SI NO ES LA PRIMERA LINEA (ESTO SE USA PARA NO TOMAR EN CUENTA LA PRIMERA LINEA DEL ARCHIVO)
			if linenumber != 0:
				linenumber += 1
				strline = str(line)
				list_fields = strline.split(',')
				#print('list_fields[0]: ', list_fields[6])
				
				#ELIMINA EL CARACTER DE INICIO DE LINEA EL CUAL ES <b>
				#SE USA CUANDO EL CARACTER INICIAL SE SEPARA POR UNA " [COMILLA DOBLE] DEL VALOR DEL PRIMER CAMPO ("B"NNNN")
				#si si la comilla es simple
				if  list_fields[0].find('\'') != -1:
					id_departamentoList = list_fields[0].split('\'')
				#SE USA CUANDO EL CARACTER INICIAL SE SEPARA POR UNA ' [COMILLA SIMPLE] DEL VALOR DEL PRIMER CAMPO ("B"NNNN")
				else:
					id_departamentoList = list_fields[0].split('\"')
				
				#ASIGNAMOS EL VALOR NUMERICO DEL PRIMER CAMPO OBTENIDO
				cod_localidad = id_departamentoList[1]
				#SI EL TAMAÑO DE LA LISTA DE CAMPOS ES MAYOR QUE UN MINIMO ENTONCES CREO UN OBJETO ESPACIO PUBLICO CON SUS VALORES CORRESPONDIENTES
				if len(list_fields) > 22:
					space1 = EspaciosPublicos(cod_localidad=cod_localidad, 
												id_provincia=list_fields[1], 
												id_departamento=list_fields[2],
												categoria = normalize(list_fields[4]),
												record_type = record_type_name,
												provincia = normalize(list_fields[6]),
												localidad = normalize(list_fields[7]),
												nombre = normalize(list_fields[9]),
												codigo_postal = normalize(list_fields[11]) ,
												telefono = list_fields[12] + ' ' +list_fields[13],
												email = list_fields[14],
												web = list_fields[15],
												fuente = normalize(list_fields[21])
												)
					session.add(space1)
			#SI ES LA PRIMERA LINEA
			else:
				linenumber += 1
		
Iiterate_Spaces(URL_MUSEOS, session,'MUSEOS')
Iiterate_Spaces(URL_CINES, session, 'CINES') 
Iiterate_Spaces(URL_BIBLIOTECAS, session, 'BIBLIOTECAS')

session.commit()



#select categoria, count(id_space) from espacios_publicos group by categoria
#select fuente, count(id_space) from espacios_publicos group by fuente
#select provincia, count(id_space) from espacios_publicos group by provincia
