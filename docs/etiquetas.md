## Generación de etiquetas de lso gráficos creados

Para mostrar los datos en el eje de coordenadas X del gráfico, es necesario asignar una etiqueta para la cual se le asignará un valor. En la librería *Django-jchart* al igual que con la generación de colores de los gráficos, esta acción se hace de la misma manera, es decir, crear un array con el valor de cada etiqueta. Nuevamente, debido al uso de la aplicación, esta acción podría limitar el correcto funcionamiento de la aplicación y por consecuente la generación del gráfico. Para ello, se realicó otra función la cual generaba las etiquetas según los datos proporcionados por el usuario al realizar el experimento.

### Generación de etiquetas en Django-jchart

```python

 def get_labels(self, **kwargs):
        return ["Red", "Green", "Yellow", "Grey", "Blue"]
```
### Función creada de generación de etiquetas

```python
def labels(data):
    labelsChart = []
    for i,v in enumerate(data):
         listValues = []
         for algorithm,values in sorted(v.iteritems()):
            for step,stepvalues in sorted(values.iteritems()):
                listValues.append(str(step))
                listValues.sort(key=int)
    labelsChart= listValues
    return labelsChart
```

Esta función, recibe el diccionario con los valores del hipervolumen de cada algoritmo. Una vez se recorre cada algoritmo, se obtienen los pasos del algoritmo y se ordenan para mostrar las etiquetas en el orden correcto. Una vez se realiza esta acción, se retorna la lista con las etiquetas de los pasos.


### Función getlabels creada

```python
def get_labels(self,*args, **kwargs):

    dataModel = MinChartModel.objects.filter().latest('id')
    data = dataModel.listValues
    labelsChart=labels(data)
    return labelsChart
```