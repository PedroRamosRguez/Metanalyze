## DjangoModel

Para la creción de modelos, Django posee en su API otra potente herramienta para guardar los datos en un gestor de base de datos que se tenga configurado. Por defecto, si el usuario no introduce ningún gestor de base de datos, se utilizará por defecto el que viene integrado en Django *sqlite*

* Cada modelo en Django es una subclase de la clase ` django.db.models.Model`
* Cada atributo del modelo es un campo de la base de datos
* Con estos pasos y lo explicado anteriormente en la sección [Crear modelos y registrarlos](./modelos.md) es posible crear modelos de nuestra aplicación web en Django gracias a la potente API que posee para ello.

A continuación, se muestra un ejemplo sencillo que se puede encontrar en la [documentación del uso de modelos en Django](https://docs.djangoproject.com/en/1.11/topics/db/models/).

`models.py`
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

**first_name** y **last_name** son campos del modelo. El tipo de dato de los modelos, se define mediante el uso de `models.CharField(max_length=30)` el cual quiere decir que será un campo de texto con una máxima longitud de 30 caracteres.

Este modelo creado, generará la tabla que se muestra a continuación.

```sql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

El nombre de la tabla se genera automáticamente por el nombre de la clase. Además, cada modelo posee un identificador que será su clave primaria y es autoincremental.
