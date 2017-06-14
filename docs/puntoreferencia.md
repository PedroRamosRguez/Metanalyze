## Punto de referencia

Para realizar el cálculo del hipervolumen, es necesario calcular un punto de referencia. En esta ocasión, para la obtención del punto de referencia se ha realizado mediante el cálculo del peor punto de la coordenada **x** y la peor coordenada del eje **y**. Este punto de referencia, será el mismo para todos los algoritmos ya que al ser el peor punto de todos es el más aconsejable poner como punto de referencia.


Para realizar este cálculo, se necesita pasar el diccionario donde se guarda el contenido de las soluciones de los diferentes algoritmos y la lista donde se almacenará el punto de referencia. La lista del punto de referencia, se ha inicializado a 0 anteriormente dependiendo del número de objetivos que se haya introducido en la configuración de la ejecución de los diferentes algoritmos.

`referencePoint.py`
```python
def referencePointInit(nAlgorithms,nObjectives):
  	referencePoint = []
	for i in range(nObjectives):
		referencePoint.append(0)
	return referencePoint

def referencePointCalculation(dicAlg,referencePoint):
	for k,v in sorted(dicAlg.iteritems()):
		for execution,executionvalue in sorted(v.iteritems()):
			for step,stepvalue in sorted(executionvalue.iteritems()):
				for x,value in enumerate(stepvalue):
					maxX = float(value[0])
					maxY = float(value[1])
					if maxX > referencePoint[0]:
						referencePoint[0] = maxX
					if maxY > referencePoint[1]:
						referencePoint[1] = maxY
				
	 #referencePoint = val
	return referencePoint
```

Este método es cambiable ya que en esta ocasión sólo se tienen en cuenta coordenadas máximas para dos objetivos.