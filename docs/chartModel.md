## Modelos para los diferentes gráficos creados

Este modelo, está dividido en varios modelos diferenciando el tipo de gráfico que se mostrará al usuario. Los nombres de los modelos son los siguientes:

* MinAvgMaxChartModel
* MinChartModel
* AvgChartModel
* MaxChartModel

En caso de que el usuario seleccione la salida de datos como gráfico, se tendrá en cuenta qué tipo de rendimiento de hipervolumen seleccionó el usuario. En caso de que seleccione *mínimo*,*media* y *máximo* se utilizará el modelo `MinAvgMaxChartModel` para crear el gráfico con todos los resultados. Mientras que el resto de modelos, se utilizará exclusivamente si el usuario selecciona la opción correspondiente al cálculo del rendimiento del hipervolumen.

```python
class ChartsModel(models.Model):
    listValues = ListField()
    configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)
```

Los modelos están compuesto por la clave foránea al identificador de la configuración y una lista de valores donde se guardarán los datos de los gráficos.