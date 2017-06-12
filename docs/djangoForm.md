## DjangoForm

Django form es una API incluida en Django para la creación de formularios. 

El uso de formularios en aplicaciones webs es algo fundamental para el correcto funcionamiento de la misma, por tanto, para la creación de formularios en aplicaciones Django basta con utilizar esta API importando el módulo *forms* de Django `from django import forms`.

Una vez se importa este módulo, es posible generar cualquier elemento que se utilice en un formulario (campos de texto, listas desplegables, radio buttons, checkbox, etc).

El siguiente ejemplo, es el que se muestra [en la documentación de Django](https://docs.djangoproject.com/en/1.11/topics/forms/) para introducirse en la creación de formularios utilizando la API de Django.

### Formulario en la template

```html
<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>
```

### Formulario creado con Django Form
`forms.py`
```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

Con la creación del formulario en Django mediante el uso de Django Form y la creación del template, es posible mostrar con una interfaz sencilla y entendible para el usuario de que debe rellenar el campo con su nombre.

Al ser una petición *post*, en el lado servidor se debe aceptar el formulario, para ello, django form posee de una función llamada **is_valid()**. Esta función debe devolver *True* para permitir la introducción de los datos en el formulario y continuar con la ejecución de la aplicación.