## Modelos para la escritura de resultados estadísticos

Este modelo, está dividido en varios modelos diferenciando el tipo de fichero donde se escribirán los resultados de los tests estadísticos.

* StatisticDataframeTex
* StatisticDataframeTxt
* StatisticDataframeHtml

Como los resultados estadísticos se muestran con una serie de iconos, para mostrarlos en los diferentes formatos de salida se debe utilizar una codificación diferente, por tanto, para tener mayor control se creó un modelo para cada tipo de salida de datos.

```python
class StatisticDataframeTex(models.Model):
    listValues = ListField()
    configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)
```

Los modelos están compuesto por la clave foránea al identificador de la configuración y una lista de valores donde se guardarán los símbolos de los resultados de los test estadísticos.