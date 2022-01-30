#DEBE INSTALAR PREVIAMENTE EN SU COMPUTADORA

-python version 3 o superior

-Postgresql vesion 14

#DEBE INSTALAR LOS MODULOS DE PYTHON USANDO LOS SIGUIENTES COMANDOS

pip install requests 

pip install sqlalchemy

#PARA EJECUTAR EL ARCHIVO

python data_loader.py

#RESULTADOS

En la seccion public de su base de datos debe crearse dos tablas con los siguientes datos:

Tabla: Espacios_publicos
Campos:
-cod_localidad
-id_provincia
-id_departamento
-categoría
-provincia
-localidad
-nombre
-domicilio
-código postal
-número de teléfono
-mail
-web

Tabla: resumen_cines
Campos: 
-Provincia
-Cantidad de pantallas
-Cantidad de butacas
-Cantidad de espacios INCAA


#PARA OBTENER DATOS ADICIOANLES COMO ESTOS:

-Cantidad de registros totales por categoría

-Cantidad de registros totales por fuente

-Cantidad de registros por provincia y categoría

Puede usar lo siguiente

select categoria, count(id_space) from espacios_publicos group by categoria

select fuente, count(id_space) from espacios_publicos group by fuente

select provincia, count(id_space) from espacios_publicos group by provincia

