##Creación del formulario de la aplicación

Para crear el formulario que se muestra en la pantalla de inicio, se creó la clase `class AlgorithmForm(forms.Form):` la cual utiliza la clase Form de la API de Django. Para poder utilizar la Django Form, es necesario importar el módulo ya que si no dará un error `from django import forms`

Para crear las opciones de los diferentes **radio buttons** que posee el formulario, se crearon de la siguiente forma:

```python
CHOICES_dataOutput = (
        ('table', 'Table'),
        ('plot', 'Plot'),
        ('table-plot', 'Table and Plot'),
    )
    CHOICES_statisticTest =(
        ('yes','yes'),
        ('no','No')
    )
    CHOICES_evaluations =(
        ('Number_of_evaluation','Number of evaluation'),
        ('Time','Time')
    )
```

Gracias a la API de Django Form que posee el framework, es posible generar de esta manera tan fácil las opciones que se deseen en un radio button.

Para generar el radio button como tal y se muestre en nuestro formulario es necesario configurarlo. Para configurar por ejemplo el de **statisticTest**, se realizó de la siguiente manera:

`statisticTest = forms.ChoiceField(widget=forms.RadioSelect(attrs = {'class': 'with-gap dataOutput'}),choices=CHOICES_statisticTest, required=True)`

Esto lo que permite hacer es crear un radio button con el nombre statisticTest, el cual mediante el uso de `forms.ChoiceField(widget=forms.RadioSelect` se le dice a la API que es un botón tipo radio y mediante los atributos que se le añaden con `attrs = {'class': 'with-gap dataOutput'}),choices=CHOICES_statisticTest, required=True)` se crea con el nombre de cierta clase y con las elecciones que se configuraron anteriormente en **CHOICES_statisticTest** y además, con el uso de *required=True* se exige que este campo se debe rellenar obligaroriamente.

Para la creación del campo de texto idAlgorithm, se realizó de la siguiente manera:

`idAlgorithm = forms.CharField(widget = forms.TextInput(attrs={'id':'idAlgorithm',
        'placeholder':'Introduce the identificator for this algorithm','oninput':'configureAlgorithm()'}),required=False)`

Esto crea un campo de texto con el identificador *idAlgorithm* con el placeholder `Introduce the identificator for this algorithm` y con un evento oninput el cual llama a una función de un fichero *Javascript* llamada configureAlgorithm. 