## Generación de ficheros txt

Para la generación de los resultados del hipervolumen por paso de cada algoritmo, se realiza de una manera más simple. En esta ocasión, lo que se realiza es convertir a texto y añadirle a la cadena a insertar en el fichero un formato e ir insertando los valores de las celdas del *DataFrame*. Los pasos serían los siguientes:

* A partir del conjunto de datos del algorimo iésimo, obtener los valores de las columnas
* Recorrer las filas del *DataFrame*
* Crear una cadena con un formato inicial
* Insertar en la cadena el valor de la columna
* Insertar los valores de las filas seguido de espacios
* Finalmente, entre paso y paso añadir un salto de línea

Formato final del fichero txt con el cáculo del hipervolumen mínimo, medio y máximo

```
200 0.79439511239 0.998543022631 0.0 
400 0.895777258487 0.999075300315 0.342524938889
.
.
30000 0.999202223859 0.999987945215 0.99151801094 
```

Código para generar ficheros con extensión *.txt*

```python
for i,v in enumerate(df):
        columns = df[i].columns.values
        stringFormat = str(algorithm_names[i])+'Results'+'\n'
        for index,row in df[i].iterrows():
          stringFormat = str(index)+' '
          for j,v in enumerate(columns):
            stringFormat = stringFormat + str(row[str(v)])+' '
          stringFormat = stringFormat + '\n'
          with open(os.path.join(mediafolder,str(algorithm_names[i])+'.txt'), 'a') as myfile:
            myfile.write(str(stringFormat))
```
Se generará un fichero txt por cada uno de los algoritmos a comparar.

## Fichero txt con resultados estadísticos

Para la creción del fichero de texto con los resultados obtenidos de la comparación entre diferentes metaheurísticas se realiza de la siguiente manera:

```python
txtfilename = os.path.join(mediafolder,'statisticalResults.txt')
      	statisticDftxt.to_csv(txtfilename, header=statisticDftxt.columns.values, index=True, sep=' ', mode='a')

```

El nombre del fichero será *statisticalResults.txt* en la carpeta media. El siguiente paso será mediante la función `to_csv()` que posee **Pandas** generar el fichero en concreto. La configuración que se le ha pasado es la de añadir en los encabezados las columnas del dataframe y mediante la orden `index=True` se le dice a la función que añada también los valores de las filas.
