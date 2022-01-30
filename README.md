#DEBE INSTALAR PREVIAMENTE EN SU COMPUTADORA

-python version 3 o superior

-Postgresql vesion 14

#DEBE INSTALAR LOS MODULOS DE PYTHON USANDO LOS SIGUIENTES COMANDOS

pip install requests 

pip install sqlalchemy

#PARA EJECUTAR EL ARCHIVO

python data_loader.py

#RESULTADOS

En la seccion public de su base de datos debe crearse una tabla denominada Espacios_publicos
la cual contendra los siguientes datos:

o cod_localidad
o id_provincia
o id_departamento
o categoría
o provincia
o localidad
o nombre
o domicilio
o código postal
o número de teléfono
o mail
o web

#PARA OBTENER DATOS ADICIOANLES COMO ESTOS:

-Cantidad de registros totales por categoría

-Cantidad de registros totales por fuente

-Cantidad de registros por provincia y categoría

Puede usar lo siguiente

select categoria, count(id_space) from espacios_publicos group by categoria 
select fuente, count(id_space) from espacios_publicos group by fuente 
select provincia, count(id_space) from espacios_publicos group by provincia
