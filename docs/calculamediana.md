## Cálculo de la mediana de los datos

Para realizar el cálculo de las medianas en la aplicación, se debe importar el módulo *numpy* de **Python** el cual se importa de la siguiente manera:

`import numpy as np`

Esto importara el módulo numpy al cual se le asigna un alia *np*. Una vez se importa esta librería, es necesario llamar a la función *median()*. La función que realiza el cálculo de las medianas del conjunto de soluciones es el siguiente:

```python
def calculeMedian(hyperVolumeList):
	medianAlgorithms = []
	for i,v in enumerate(hyperVolumeList):
		npAlgorithm = np.array(v)
		#print npAlgorithm
		medianAlgorithms.append(np.median(npAlgorithm))
	return medianAlgorithms
```

Esta función recibe como parámetro una lista de listas con los datos del hipervolumen de cada algoritmo. Lo primero que se hace es crear una lista vacía donde se guardarán los valores de las medianas de cada conjunto de datos de cada algoritmo. Posteriormente, se transforma en un array de *Numpy* la lista actual de valores de hipervolumen y se realiza el cálculo de la mediana para el conjunto de soluciones del algorimo iésimo. Finalmente, se retorna una lista con las medianas de los algoritmos a comparar.