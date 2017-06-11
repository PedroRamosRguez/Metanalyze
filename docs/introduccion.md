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

En caso de que no cree algún fichero o algún directorio se deberá crear manualmente.