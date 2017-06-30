![Logo MetAnalyze](app/static/image/logo.png)

## Aplicacion TFG 

Herramienta desarrollada mediante el framework [Django](https://www.djangoproject.com/) para la realización del **Trabajo de fin de Grado** del Grado de Ingeniería Informática en la Universidad de La Laguna (ULL).

## Autor de la aplicación
[Pedro Manuel Ramos Rodríguez](http://alu0100505078.github.io/)


## División de directorios app

* El directorio *appTFG* es el nombre del proyecto creado en Django mediante el comando`django-admin startproject mysite`

* El directorio *app* es la aplicación creada en Django mediante el comando `python manage.py startapp app`
* El directorio *docs* es donde se guarda la documentación del proyecto para generar el gitbook del mismo
* Y finalmente, el directorio *media* es donde se guardarán los ficheros que se generen al realizar el experimento con la aplicación y que posteriormente se descargarán si el usuario lo desease.

## Instalar paquetes utilizados

Para instalar todos los paquetes utilizados en el proyecto debe instalarlos mediante el siguiente comando:

```bash
$ pip install -r requirements.txt
```