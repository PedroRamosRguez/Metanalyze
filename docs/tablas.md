## Generación de tablas

Para la generación de las diferentes tablas a mostrar en la aplicación se ha utilizado la librería *Pandas* que posee **Python**. Para utilizar esta librería, primero hay que importarla `import pandas as pd`. Esta línea permite cargar la librería pandas y asignarle un alias *pd* para su uso.

Pandas permite generar una tabla con filas y columnas a partir de un conjunto de datos. Para ello, lo primero que se realiza es llamar a la función `DataFrame()` que posee esta librería. Una vez el *DataFrame* está creado, se permitirá realizar multiples acciones con los datos.

## Generación de DataFrame de datos de hipervolumen

Para la generación de los diferentes dataframes, se han utilizado una serie de funciones las cuales cada una genera un *DataFrame* de un conjunto de datos determinados.

Para generar la tabla con los diferentes pasos y el resultado de los hipervólumenes por paso, se utiliza la siguiente función:

```python
def mainDataFrame(dictHvAlg):
	df = []
	for k,v in sorted(dictHvAlg.iteritems()):
		df.append(pd.DataFrame(v))
  	return df
```

Esta función obtine el diccionario con los datos por paso del cálculo de hipervolumen y genera a partir de estos datos un *Pandas DataFrame*.

## Generación de DataFrame de gráficos

Para guardar los datos de los gráficos a crear, se utilizan una serie de funciones que se detallan a continuación:

```python
def minAvgMaxDataFrame(df):
	dfMinAvgMax = []
	for i,v in enumerate(df):
		dfMinAvgMax.append(pd.DataFrame(v.min(),columns=['Min']))
		dfMinAvgMax[i]['Average']=v.mean()
		dfMinAvgMax[i]['Max'] = v.max()
	return dfMinAvgMax
```

```python
def minDataFrame(df):
	dfMin = []
	for i,v in enumerate(df):
		dfMin.append(pd.DataFrame(v.min(),columns=['Min']))
	return dfMin
```

```python
def avgDataFrame(df):
	dfAvg = []
	for i,v in enumerate(df):
		dfAvg.append(pd.DataFrame(v.mean(),columns=['Avg']))
	return dfAvg
```

```
def maxDataFrame(df):
	dfMax = []
	for i,v in enumerate(df):
		dfMax.append(pd.DataFrame(v.max(),columns=['Max']))
```

Cada una de estas funciones recibe como parámetro el dataframe principal con los datos de los hipervólumenes por paso de los algoritmos a comparar.

Finalmente, cuando los diferentes dataframes están generados, se procederá a guardar los datos en los modelos correspondientes a cada uno de estos *DataFrames*. 

## Almacenamiento de DataFrames en modelos

Para guardar los diferentes *DataFrames* en los modelos correspondientes, se convertirán estos dataframes en diccionarios con la llamada a la función `DataFrame.to_dict()` que posee **Pandas**. En esta ocasión, esta operación se realizó en diferentes funciones para el almacenamiento de cada uno de los conjuntos de datos en los diferentes modelos.

```python
def setMinAvgMaxChart(dfMinAvgMax,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMinAvgMax):
		modeList.append(v.to_dict())
	cModels.modelMinAvgMaxCharts(idConfiguration,modeList)
```

```python
def setMinChart(dfMin,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMin):
		modeList.append(v.to_dict())
	cModels.modelMinCharts(idConfiguration,modeList)
```

```python
def setAvgChart(dfAvg,idConfiguration):
	modeList = []
	for i,v in enumerate(dfAvg):
		modeList.append(v.to_dict())
	cModels.modelAvgCharts(idConfiguration,modeList)
```

```python
def setMaxChart(dfMax,idConfiguration):
	modeList = []
	for i,v in enumerate(dfMax):
		modeList.append(v.to_dict())
	cModels.modelMaxCharts(idConfiguration,modeList)
```

Cada una de estas funciones recibirá por parámetro el *DataFrame* correspondiente y el identificador de la configuración del experimento realizado.

Debido a que el uso de diccionarios genera los datos de manera desordenada, la creación de estos dataframes como diccionarios también se generan de manera desordenada. Por tanto, para dar un orden a los datos y que éstos estén ordenados por el número del paso donde el algoritmo volcó el conjunto de soluciones, se creó una función para ordenar los datos generados por los *DataFrames*.

## Ordenación de los datos de los dataframes

```python
def sortAvgDataframe(dic):
	sortedbyKeys = sorted(dic, key = lambda tup:int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns=['Step','Average']
	return df
```

```python
def sortMaxDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns = ['Step','Max']	
	return df
```

```python
def sortMinDataframe(dic):
	sortedbyKeys = sorted(dic, key=lambda tup: int(tup[0]),reverse=False)
	index = []
	for i,v in enumerate(sortedbyKeys):
		index.append(str(v[0])) 
	df = pd.DataFrame(sortedbyKeys,index=index)
	df.columns = ['Step','Min']
	return df
```

Estas funciones reciben por parametro el diccionario que se obtiene de los diferentes modelos y se realizan una serie de acciones. Estas acciones son:

* Ordenar las claves del diccionario recibido mediante la función `sorted(dic, key=lambda tup: int(tup[0]),reverse=False)`

* El siguiente paso, será realizar el *DataFrame* de los datos ordenados con el paso como índice de las filas y las columnas pertinentes.

* Finalmente, se retorna el dataframe creado.

La llamada a estas funciones, se realizará desde la vista para posteriormente generar la tabla **HTML** de los datos obtenidos del hipervolumen por paso de cada algoritmo.


## Generación resultados estadísticos formato txt

Para generar las tablas con los resultados estadísticos obtenidos a formato texto para almacenarlos en ficheros *.txt* se realizó con la siguiente función:

```python

def statisticDataframetxt(algorithm_names,value,meanAlgorithms,medianAlgorithms):
  statisticDftxt = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
  for i,v in enumerate(value):
    j=i+1
    while j < int(len(algorithm_names)):
      statisticDftxt.set_value(algorithm_names[i],algorithm_names[i],'=')
      statisticDftxt.set_value(algorithm_names[j],algorithm_names[j],'=')
      if(v[1] < 0.05):
        #statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
        if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif medianAlgorithms[i] < medianAlgorithms[j]:
          #algoritmo1 mejor que algoritmo2
          statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'+')
          statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'-')
        elif medianAlgorithms[i] > medianAlgorithms[j]:
          #algoritmo1 peor que algoritmo2
          statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'-')
          statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'+')
      else:
        #no existen diferencias
        statisticDftxt.set_value(algorithm_names[i],algorithm_names[j],'=')
        statisticDftxt.set_value(algorithm_names[j],algorithm_names[i],'=')
      j+=1
  return statisticDftxt
```

Este paso se realiza una vez se han realizado los diferentes test estadísticos. La función obtine por parámetros:

* Una lista con los nombres de los diferentes algoritmos a comparar
* Una lista con los valores estadísticos de cada uno de los algoritmos
* El resultado de las medias de los diferentes algoritmos
* El resultado de las medianas de los algoritmos

Lo que se comprobará es el p valor de cada uno de los algoritmos. En caso de que sea *< 0.05*, se realizarán las comparaciones entre un algoritmo y el resto.

El formato de si un algoritmo es estadísticamente mejor o peor, cambiará dependiendo del tipo de fichero generado, este es el principal motivo por el cual se han generado diferentes funciones para la creación de *DataFrames* con'símbolos diferentes.


## Generación resultados estadísticos formato Latex

```python
def statisticDataframetex(algorithm_names,value,meanAlgorithms,medianAlgorithms):
  statisticDftex = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
  for i,v in enumerate(value):
    j=i+1
    while j < int(len(algorithm_names)):
      statisticDftex.set_value(algorithm_names[i],algorithm_names[i],'$\leftrightarrow$')
      statisticDftex.set_value(algorithm_names[j],algorithm_names[j],'$\leftrightarrow$')
      if(v[1] < 0.05):
        #statisticDftex.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
        if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
          #caso especial se inserta un asterisco
          statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'*')
          statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'*')
        elif medianAlgorithms[i] < medianAlgorithms[j]:
          #algoritmo1 mejor que algoritmo2
          statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\uparrow$')
          statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\downarrow$')
        elif medianAlgorithms[i] > medianAlgorithms[j]:
          #algoritmo1 peor que algoritmo2
          statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\downarrow$')
          statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\uparrow$')
      else:
        #no existen diferencias
        statisticDftex.set_value(algorithm_names[i],algorithm_names[j],'$\leftrightarrow$')
        statisticDftex.set_value(algorithm_names[j],algorithm_names[i],'$\leftrightarrow$')
      j+=1
  return statisticDftex
```

## Generación resultados estadísticos formato HTML


```python
def statisticDataframeHtml(algorithm_names,value,meanAlgorithms,medianAlgorithms):
  statisticDfhtml = pd.DataFrame(index=algorithm_names,columns=algorithm_names)
  for i,v in enumerate(value):
      j=i+1
      while j < int(len(algorithm_names)):
        statisticDfhtml.set_value(algorithm_names[i],algorithm_names[i],u'\u2194')
        statisticDfhtml.set_value(algorithm_names[j],algorithm_names[j],u'\u2194')
        if(v[1] < 0.05):
          if meanAlgorithms[i] > meanAlgorithms[j] and medianAlgorithms[i] < medianAlgorithms[j]:
            #caso especial se inserta un asterisco
            statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],'*')
            statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],'*')
          elif meanAlgorithms[i] < meanAlgorithms[j] and medianAlgorithms[i] > medianAlgorithms[j]:
            #caso especial se inserta un asterisco
            statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],'*')
            statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],'*')
          elif medianAlgorithms[i] < medianAlgorithms[j]:
            #algoritmo1 mejor que algoritmo2
            statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2191')
            statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2193')
          elif medianAlgorithms[i] > medianAlgorithms[j]:
            #algoritmo1 peor que algoritmo2
            statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2193')
            statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2191')
        else:
          #no existen diferencias
          statisticDfhtml.set_value(algorithm_names[i],algorithm_names[j],u'\u2194')
          statisticDfhtml.set_value(algorithm_names[j],algorithm_names[i],u'\u2194')
        j+=1
  return statisticDfhtml
```

## Almacenamiento de resultados estadísticos en modelos

Al igual que se realiza con los *DataFrames* creados para los resultados del hipervolumen por paso de cada uno de los algoritmos, también se guardarán los dataframes creados para la generación de los ficheros de salida con los resultados estadísticos obtenidos. Se dividen en tres funciones diferentes para cada uno de los formatos de salida de los resultados.

```python
def setStatisticalDfTex(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfTex(idConfiguration,modeList)
```

```python
def setStatisticalDfTxt(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfTxt(idConfiguration,modeList)
```

```python
def setStatisticalDfHtml(statisticalDf,idConfiguration):
	modeList = []
	modeList.append(statisticalDf.to_dict())
	cModels.modelStatisticalDfHtml(idConfiguration,modeList)
```