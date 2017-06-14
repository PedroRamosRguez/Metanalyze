## Librería Django-jchart

Para la generación de los resultados en forma de gráficos se utiliza la librería [*Django-jchart*](https://github.com/matthisk/django-jchart). Esta librería, es una implementación en **Python** de la librería *ChartJs* de **Javascript**. Para la utilización de la librería, es necesario "comunicarle" a Django que utilice este módulo. Para ello, se añadió en la configuración de **Django** en el apartado *INSTALLED_APPS=* el módulo de jchart.

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'jchart',
)
```
Y en el lado cliente, se debe añadir el siguiente script:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.bundle.min.js"></script>
```

Una vez se ha añadido en la configuración la introducción de la librería, hay que crear un fichero con la importación de *Django-jchart* y los componentes que se vayan a utilizar de la librería.

```python
from jchart import Chart
from jchart.config import DataSet,Axes,Legend
class MinChart(Chart):
chart_type = 'line'
    scales = {
        'yAxes': [{'scaleLabel':{'display':True,'labelString':'Hypervolume','fontSize':int(15)}}],
        'xAxes' : [{'scaleLabel':{'display':True,'labelString':str(getConfiguration.evaluation),'fontSize':int(20)}}]
        
    }

    title = {
        'display': True,
        'text': 'Evolution of Minimum Hypervolume',
        'fontSize': 20,
    }
    legend = {
        'display': True,
        'position': 'right'
    }
    responsive = True
```

En este pequeño código, se ha creado una clase para la creación del gráfico con la evolución del hipervolumen mínimo el cual se ha configurado el eje de coordenadas x e y, el título que aparece en la parte superior del gráfico, la aparición y la colocación de la leyenda y la posibilidad de que el gráfico sea responsivo.

