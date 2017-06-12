## Modelo de la configuración

Para guardar los datos que el usuario introduce en el formulario de la pantalla inicial, es necesario guardar los datos en modelos. Los datos introducidos serán guardado en diferentes modelos para tener un orden de los datos que el usuario introduce.

El *configurationModel* será el modelo más importante. Este modelo, permitirá guardar los datos de configuración de la ejecución de los algoritmos para resolver el problema de optimización multi-objetivo dado. Además, debido a que todos los algoritmos que se comparen han utilizado la misma configuración, los demás modelos tendrán una clave foránea a la clave principal de este modelo. El modelo está compuesto de la siguiente manera:

```python
class Configuration(models.Model):
  nAlgorithms = models.CharField(max_length = 100) #Numero de algoritmos
  nObjectives = models.CharField(max_length = 100)  #Numero de objetivos que se utiliza para el analisis del algoritmo
  nExecutions = models.CharField(max_length = 100) #Numero de ejecuciones realizadas para las pruebas del algoritmo
  step = models.CharField(max_length = 100)        #Numero del paso del analisis del algoritmo. Ej; cada 200
  stopCondition = models.CharField(max_length = 100) #Condicion de parada para el analisis del algoritmo
  dataOutput = models.CharField(max_length = 100)   #Formato de salida de datos despues de realizar el analisis(grafico,tabla o ambas)
  bound =  ListField()#models.CharField(max_length = 100)        #Guardara la opcion de calcular en la metrica: minimo, media o maximo
  metric =  ListField()#models.CharField(max_length = 100)       # Guarda la metrica o metricas que se analizaran
  statisticTest = models.CharField(max_length = 2)
  evaluation = models.CharField(max_length = 100)     #guarda el titulo del ejex del grafico
```