## Parsear ficheros .tar

Para realizar el parseo de los ficheros con extensión *.tar* se utilizó el módulo **Tarfile** de Python. Este paquete, permite trabajar con ficheros extensión *.tar* y *.tar.gz*.

Cómo la librería funciona de diferentes maneras en caso de que el fichero sea de un tipo o de otro es necesario comprobar la extensión del mismo. Para comprobarlo se utilizan expresiones regulares. Para poder trabajar con expresiones regulares en python y realizar una serie de operaciones con las cadenas resultantes, es necesario importar el módulo *re*.

```python
for i,fileName in enumerate(files):
	fileList = []  #lista donde se guardara la lista de ficheros que tenga ese tarfile o zipfile.
	if re.search(r'^[\w+\s*\d*]+\.{1}tar\.{1}gz$',fileName):
		#fichero tipo tar.gz
		tar = tarfile.open(dir+str(fileName),'r:gz')
		for member in tar.getmembers():
			fileList.append(member)
		
		sortedByFilename = sortFiles(fileList)
		fileSorted.append(sortedByFilename)
		for j,member in enumerate(fileSorted):
			dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)

	elif re.search(r'^[\w+\s*\d*]+\.{1}tar$',fileName):
		#fichero tipo tar
		tar = tarfile.open(dir+str(fileName))
		for member in tar.getmembers():
			fileList.append(member)
		
		sortedByFilename = sortFiles(fileList)
		fileSorted.append(sortedByFilename)
		
		for j,member in enumerate(fileSorted):
			dictionary = parseFiles(tar,i,dicAlg,member,getConfiguration)

```

El código recorre la lista de nombre de ficheros que se han subido al servidor, en caso de que se detecte que es un fichero *.tar* con la condición `elif re.search(r'^[\w+\s*\d*]+\.{1}tar$',fileName):`, se crea un objeto y se recorre el interior del fichero comprimido y se parsea.

## Parsear ficheros .tar.gz

En caso que el fichero sea con extensión *.tar.gz* la operación es algo distinta pero el resultado es el mismo. Mediante la condición `if re.search(r'^[\w+\s*\d*]+\.{1}tar\.{1}gz$',fileName):`se detecta que es un fichero de este tipo. A continuación, se crea el objeto `tar = tarfile.open(dir+str(fileName),'r:gz')` y se recorre su interior para posteriormente parsearlos.