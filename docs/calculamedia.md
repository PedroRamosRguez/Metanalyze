## Cálculo de la media de los datos

Para concluir con el análisis estadístico es necesario calcular las medias y las [medianas](./calculamediana.md) del conjunto de soluciones que generan los algoritmos utilizados para resolver cierto problema. Para realizar el cálculo de las medias en la aplicación, se debe importar el módulo *numpy* de **Python** el cual se importa de la siguiente manera:

`import numpy as np`

Esto importara el módulo numpy al cual se le asigna un alia *np*. Una vez se importa esta librería, es necesario llamar a la función *mean()*. La función que realiza el cálculo de las medias del conjunto de soluciones es el siguiente:

```python
def calculeMean(hyperVolumeList):
	meanAlgorithms = []
	for i,v in enumerate(hyperVolumeList):
		npAlgorithm = np.array(v)
		#print npAlgorithm
		meanAlgorithms.append(npAlgorithm.mean())
	return meanAlgorithms
```
Esta función recibe como parámetro una lista de listas con los datos del hipervolumen de cada algoritmo. Lo primero que se hace es crear una lista vacía donde se guardarán los valores de las medias de cada conjunto de datos de cada algoritmo. Posteriormente, se transforma en un array de *Numpy* la lista actual de valores de hipervolumen y se realiza el cálculo de la media para el conjunto de soluciones del algorimo iésimo. Finalmente, se retorna una lista con las medias de los algoritmos a comparar.
