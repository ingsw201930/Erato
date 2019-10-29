# Erato

Proyecto realizado por Silver Steel Systems

Repositorio del proyecto Erato, para la materia ingenieria de software

Creando el usuario en Postgresql para django

Podemos observar que el usuario es “postgres”, este es un usuario creado en la instalación de postgres. Estamos creando la base de datos con el nombre “erato”, es importante mantener este nombre porque es el escrito en el archivo de configuración.
[postgres@Sei root]$ createdb erato
“Psql” es el equivalente a “USE DATABASE_NAME” en sql, aquí estamos seleccionando la base de datos que queremos usar, ya debe haber sido creada.
[postgres@Sei root]$ psql erato
could not change directory to "/root": Permission denied
psql (11.5)
Type "help" for help.

Es importante crear el usuario con este nombre y esta contraseña, ya que es la que está configurada en el archivo de configuraciones de django. 
erato=# create user django with encrypted password 'django';
CREATE ROLE
Inicialmente se conceden todos los privilegios al usuario django, esto permite a django administrar las bases de datos a través del usuario que ya hemos creado.
erato=# grant all privileges on database erato to django;
GRANT
Para volver a la línea de comandos de linux, escribimos “quit”.
erato=# quit

Descarga del repositorio y dependencias

La descarga del repositorio se hace con el comando a continuación.
[user@Sei root]$ git clone https://github.com/ingsw201930/Erato

Python debe estar instalado, la versión usada es 3.7.4, los módulos necesarios se instalan con pip y son:
Django
Psycopg2
Simple-crypt
Pypng
stripe

Ejemplo de instalación de un módulo con pip
[user@Sei root]$ pip install django
Dentro de la carpeta ERATO, el archivo manage.py inicia y administra el servidor y la base de datos.
[user@Sei root]$ cd ERATO

[user@Sei root]$ python manage.py makemigrations

[user@Sei root]$ python manage.py migrate

[user@Sei root]$ python manage.py runserver
