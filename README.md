## Aplicacion TFG 

Herramienta desarrollada mediante el framwork [Django](https://www.djangoproject.com/) para la realización del **Trabajo de fin de Grado** del Grado de Ingeniería Informática en la Universidad de La Laguna (ULL).

## Autor de la aplicación
[Pedro Manuel Ramos Rodríguez](http://alu0100505078.github.io/)

## Creación de un proyecto en Django.

Para crear un proyecto en [Django](https://www.djangoproject.com/), lo primero que hay que realizar es el comando
`$ django-admin startproject mysite` esto creará un directorio llamado mysite en el directorio actual con la siguiente configuración:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

```

## Creación de una Aplicación en Django

Una vez se ha creado el proyecto, se debe crear la aplicación a realizar. Para crearla, lo único que hay que hacer es escribir el comando `python manage.py startapp polls`. Esto creará la aplicación llamada **polls** con el arbol de directorios y ficheros siguiente:
```polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

```   

En caso de que no cree algún fichero o algún directorio, se deberá crear a mano.

## Ejecutar la APP

Para la ejecución de la aplicación, hay que abrir una terminal y añadir el siguiente comando:

`python manage.py runserver 0.0.0.0:8080`

Esto abrirá un servidor en el puerto 8080 con nuestra aplicación.

## Ejecución de los test (mirarlo mejor)

Para la realización de test unitario en la aplicación, sólo hay que añadir en la terminal el siguiente comando:

`python manage.py test`


### Información extra

Para cargar los ficheros json, se utiliza un archivo .py para cada fichero Json cargado  y mediante la configuración de context_processors en `setting.py` se puede cargar en cualquier template la variable que se retorne. Esto es muy útil para poder cargar de manera dinámica en las templates sin tener que configurar nada el usuario.

*  Añadir en setting.py esa línea`'DIRS': [os.path.join(BASE_DIR, 'app/templates')],`

Esto permitirá decirle que use el context processors que se encuentra en la app de nuestro proyecto.

* Añadir además en option

 ``` 
OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'app.cargaJsonTest.jsonTest',
            'app.cargaJsonAlgoritmos.jsonAlgoritmo',
        ],
    },
```
Para cargar los ficheros esttáticos `como css o archivos javascript` se realizó una configuración en el archivo **settings.py** del proyecto.
La configuración realizada es la siguiente:

* Crear una carpeta llamada static dentro de la carpeta del proyecto `app/static/`

* Añadir en setting.py la `STATIC_URL = '/static/'` que se realiza para poder cargar los ficheros que se encuentren en la carpeta **Static**

* El siguiente paso es añadir el directorio de los ficheros estáticos, es decir, la ruta donde se cargarán esos ficheros que se encontrarán en la carpeta **static**. En este caso, la carpeta estará dentro del directorio de nuestra aplicación que hemos llamado app. Además, para poder realizar la carga de ficheros estáticos desde nuestras templates mediante el comando `{% load static %}` se debe poner la static root `STATIC_ROOT = os.path.join(BASE_DIR, 'app/staticfiles')` que cargará los ficheros estáticos mediante la ruta actual que se guarda en la variable `BASE_DIR` y se le añade la ruta `app/staticfiles`
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'app/staticfiles')

```

Para la creación de la carpeta media y aceptar la subida de ficheros al servidor, hay que realizar una configuración previa dentro del proyecto en sí. La configuración realizada es la siguiente:

```
MEDIA_ROOT = os.path.join(BASE_DIR,'app/media')
MEDIA_URL = '/media/'

```

### Añadir los modelos y registrarlos

Para el registro de los modelos creados en la aplicación y poder guardar datos en la base de datos se deben seguir una serie de pasos:

* Añadir a setting.py en `INSTALLED_APPS` la localización de los modelos, en caso de que sea en el directorio de la aplicación, añadir el nombre de la aplicación 
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
)
```

* EL siguiente paso'será introducir una serie de comandos para realizar la migración y creación de las tablas sql:
    * `python manage.py makemigrations [nombre que se añadió en settings.py]`
    * `python manage.py sqlmigrate [nombre que se añadió en settings.py] 000X`
    * `python manage.py migrate`

* Finalmente,se debe registrar el o los modelos creados. Para el registro de los modelos, se debe añadir en admin.py las siguientes líneas:
    ```
    from .models import nombreModelo1,nombreModelo2
    admin.site.register(nombreModelo1)
    admin.site.register(nombreModelo2)
    ```






### TODO

Parsear los ficheros que llegan a la carpeta media del servidor. 
Implementar los scripts para el parseo de los fichero y el futuro tratamiento de los datos.
Implementar el hipervolumen, y mirar cómo se realizará el tratamiento de los datos para implementarlo.

Cosas a insertar en requeriments.txt
django-jchart
numpy
pandas
re
collections
tarfile
os
ast