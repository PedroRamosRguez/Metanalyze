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
