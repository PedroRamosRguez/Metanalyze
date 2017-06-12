## Modelo de los algoritmos

Este modelo se utilizará para la configuración del apartado algoritmos de la aplicación. Está compuesto de la siguiente manera:

```python
class Algorithms(models.Model):
  
  algorithm = models.CharField(max_length = 100)   #Nombre del algoritmo
  idAlgorithm = models.CharField(max_length = 100) #Guarda el identificador que se le de al algoritmo. Ej: NSGA2_90_6_5
  fileName = models.CharField(max_length = 100)    #Nombre del fichero adjunto
  nVariablesAlgorithm = models.CharField(max_length = 100) # Numero de variables que posee el algoritmo a analizar.
  configuration = models.ForeignKey(Configuration,on_delete=models.CASCADE)
  hypervolumeValues = ListField()
  ```

  Se creará una instancia de esta clase por cada algoritmo introducido para comparar. Este modelo está compuesto por :

  * El nombre del algoritmo
  * El identificador (alias) que introduzca el usuario para realizar las comparativas
  * El nombre del fichero que se adjuntó. Esto se utilizará para el parseo de los ficheros al subirlo al servidor.
  * El número de variables del algoritmo al realizar la ejecución del mismo para la resolución del problema.
  * La clave foránea al identificador del modelo de configuración. Se utiliza para saber a qué configuración pertenece. Además, está configurado para que en caso de que su configuración se elimine también se eliminen los algoritmos que utilizan esa configuración.
  * Y el último campo, será una lista con los valores del hipervolumen obtenido. Esto se utilizará para la generación de los datos gráficos y para la realización de las comparativas estadísticas.