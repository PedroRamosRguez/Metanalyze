### Carga de ficheros

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

* El siguiente paso es añadir el directorio de los ficheros estáticos, es decir, la ruta donde se cargarán esos ficheros que se encontrarán en la carpeta **static**. En este caso, la carpeta estará dentro del directorio de nuestra aplicación que hemos llamado app. Además, para poder realizar la carga de ficheros estáticos desde nuestras templates mediante el comando  load static (utilizándolo entre {} y % antes y al final) se debe poner la static root `STATIC_ROOT = os.path.join(BASE_DIR, 'app/staticfiles')` que cargará los ficheros estáticos mediante la ruta actual que se guarda en la variable `BASE_DIR` y se le añade la ruta `app/staticfiles`

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