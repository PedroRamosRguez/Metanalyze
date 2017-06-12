## Parsear ficheros con extensión .zip

En caso de que el fichero subido al servidor sea extensión *.zip*, se debe utilizar otro módulo diferente llamado *zipfile*.
El funcionamiento de esta librería, es muy similar al módulo *tarfile* con ciertas diferencias.
Para la detección del fichero *.zip* se utiliza una expresión regular. Para poder trabajar con expresiones regulares en python y realizar una serie de operaciones con las cadenas resultantes, es necesario importar el módulo *re*.

```python
else:
	#fichero tipo zip
	zf = zipfile.ZipFile(dir+str(fileName),'r')
	fileList = zf.namelist()
	dictionary = parseZipFiles(zf,i,dicAlg,fileList,getConfiguration)
```

En esta ocasión, a diferencia que con el [parseo de ficheros .tar y .tar.gz](./parseoTar.md), en el mismo código que se muestra en la sección, se entra en el else y se crea un objeto del tip *Zipfile* y se nombran los ficheros qincluidos en el mismo y se guardan en una lista.