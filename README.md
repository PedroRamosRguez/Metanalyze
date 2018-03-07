![Logo MetAnalyze](app/static/image/logo.png)

## Aplicacion TFG 

Herramienta desarrollada mediante el framework [Django](https://www.djangoproject.com/) para la realización del **Trabajo de fin de Grado** del Grado de Ingeniería Informática en la Universidad de La Laguna (ULL).

## Autor de la aplicación
[Pedro Manuel Ramos Rodríguez](http://alu0100505078.github.io/)


## División de directorios app

* El directorio *appTFG* es el nombre del proyecto creado en Django mediante el comando`django-admin startproject mysite`

* El directorio *app* es la aplicación creada en Django mediante el comando `python manage.py startapp app`
* El directorio *docs* es donde se guarda la documentación del proyecto para generar el gitbook del mismo
* Y finalmente, el directorio *media* es donde se guardarán los ficheros que se generen al realizar el experimento con la aplicación y que posteriormente se descargarán si el usuario lo desease. A su vez, en el interior del directorio *media* se encuentra el directorio *results* que será donde se guarden los ficheros txt,.tex y pdf del experimento realizado

## Pasos a seguir para la utilización de la aplicación.

En primer lugar, si fuera de su interés, instalar un entorno virtual para instalar en el mismo las dependencias utilizadas en la aplicación. Para crearlo realizarlo mediante el siguiente comando:

```bash
$ virtualenv <nombre del entorno virtual>
```

Cabe destacar, que para poder crear entornos virtuales, primero se debe instalar el paquete virtualenv.

### Linux y Os X:

`sudo pip install virtualenv`

Una vez instalado el virtualenv, ingresar en el directorio del reprositorio e instalar las dependencias de la aplicacion.

Para instalar todos los paquetes utilizados en el proyecto debe instalarlos mediante el siguiente comando:

```bash
$ sudo pip install -r requirements.txt
```
A continuación, debe realizar las migraciones de la aplicación mediante el siguiente comando:

```bash
$ python manage.py migrate
```

Si todo ha ido correctamente, al realizar el comando `python manage.py showmigrations`, deberá ver un listado con los nombres de las migraciones con unas cruces.

Finalmente, para arrancar un servidor con la aplicación, deberá introducir el siguiente comando:

```bash
$ python manage.py runserver 0.0.0.0:8001
```



