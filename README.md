## Aplicacion TFG 

Herramienta desarrollada mediante el framwork [Django](https://www.djangoproject.com/) para la realización del **Trabajo de fin de Grado** del Grado de Ingeniería Informática en la Universidad de La Laguna (ULL).

## Autor de la aplicación
[Pedro Manuel Ramos Rodríguez](http://alu0100505078.github.io/)

## Ejecutar la APP

Para la ejecución de la aplicación, hay que abrir una terminal y añadir el siguiente comando:

`python manage.py runserver 0.0.0.0:8080`

Esto abrirá un servidor en el puerto 8080 con nuestra aplicación.

## Ejecución de los test (mirarlo mejor)

Para la realización de test unitario en la aplicación, sólo hay que añadir en la terminal el siguiente comando:

`python manage.py test`



### TODO

  '''
    al seleccionar un algoritmo, comprobar si esta seleccionado y activar lo del archivo, 
    si hay 2 algoritmos o mas poner radio button de decir si usa diferentes archivos, 
    si dice si, seleccionar los archivos para  cada algoritmo,es decir, que añada tantos 
    botones de formulario de archivos por algoritmo seleccionado  si pone no solo mostrar 
    una entrada de fichero.
  '''

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
    },```